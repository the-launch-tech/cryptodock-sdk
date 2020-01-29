from abc import ABC, abstractmethod
from collections import deque

class CryptoDockTradeExecutor(ABC) :

    def __init__(self, args) :
        self.order_queue = deque()
        self.type = args.TYPE

    def queue_order(self, order) :
        self.order_queue.appendleft(order)

    def has_order_queued(self) :
        return self.order_queue.count() > 0

    def pop_order(self) :
        return self.order_queue.pop()

    @abstractmethod
    def execute(self) : pass
