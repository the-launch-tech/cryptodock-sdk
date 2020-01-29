from ..utils import State, Socket, Event, Meta, Response
from abc import ABC, abstractmethod
import websocket
import json
import datetime

class CryptoDockStrategy(ABC) :

    def __init__(self, args, data_handler, portfolio_manager, trade_executor, fill_storage) :
        self.port = args.TRADING_SOCKET_PORT
        self.host = args.TRADING_SOCKET_HOST
        self.strategy = json.loads(args.STRATEGY)
        self.id = self.strategy['id']
        self.status = State.LATENT
        self.meta = Meta(args)
        self.data_handler = data_handler(args)
        self.portfolio_manager = portfolio_manager(args)
        self.trade_executor = trade_executor(args)
        self.fill_storage = fill_storage(args)
        self.meta.set_start_funds(self.portfolio_manager.get_start_funds())
        super().__init__()

    def next_heartbeat(self, event, time = None) :
        self.meta.increment_cycles()
        if event == Event.FIND_SIGNAL :
            self.on_find(time)
        elif event == Event.BUILD_ORDER :
            self.on_build()
        elif event == Event.EXECUTE_ORDER :
            self.on_execute()
        elif event == Event.AUDIT_STRATEGY :
            self.on_audit()
        elif event == Event.STORE_FILL :
            self.on_store()

    def on_find(self, signal=None, time=None) :
        if signal :
            self.portfolio_manager.queue_signal(signal)
            self.send_heartbeat_response((Response.SIGNAL_QUEUED, signal))

    def on_build(self, handle_signal = None) :
        while self.portfolio_manager.has_signal_queued() :
            signal = self.portfolio_manager.pop_signal()
            if has_signal :
                order = handle_signal(signal)
            else :
                order = self.portfolio_manager.build_order_constraints(signal)
            if order :
                self.trade_executor.queue_order(order)
                self.send_heartbeat_response((Response.ORDER_QUEUED, order))

    def on_execute(self, handle_execution = None) :
        while self.trade_executor.has_order_queued() :
            pending_order = self.trade_executor.pop_order()
            if handle_execution :
                open_order = handle_execution(pending_order)
            else :
                open_order = self.trade_executor.execute(pending_order)
            self.fill_storage.update_open_orders('OPENED', open_order['id'])
            self.send_heartbeat_response((Response.ORDER_PLACED, open_order))

    def on_audit(self) : pass

    def on_store(self, handle_store=None) :
        for filled_order in self.fill_storage.get_recent_fills() :
            if handle_store :
                handle_store(filled_order)
            else :
                self.fill_storage.store(filled_order)
            self.fill_storage.update_open_orders('FILLED', filled_order['id'])
            self.send_heartbeat_response((Response.ORDER_FILLED, filled_order))

    def send_heartbeat_response(self, message) :
        self.ws.send(Socket.PING(self.id, message))

    def listen(self) :
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            Socket.URL(self.host, self.port, self.id),
            on_message=self.ws_message,
            on_error=self.ws_error,
            on_close=self.ws_close
        )
        self.ws.on_open = self.ws_open
        self.status = State.ACTIVE
        self.ws.run_forever()

    def ws_open(self) :
        self.ws.send(Socket.START_TRADING(self.id))

    def ws_message(self, message) :
        if message == Event.FINISHED_TRADING :
            self.server_finish()
        elif message == Event.TRADING_RESOLVED :
            self.server_resolved()
        else :
            if self.status == State.ACTIVE :
                self.next_heartbeat(message, datetime.datetime.now())

    def ws_error(self, error) : pass

    def ws_close(self) : pass

    def server_finish(self) :
        self.meta.set_end_time()
        self.status = State.LATENT
        self.ws.send(Socket.FINISHED_TRADING(self.id, self.meta.return_meta()))

    def server_resolved(self) :
        self.destroy()

    def destroy(self) :
        self.status = State.RESOLVED
        self.ws.close()
        self.ws = None
