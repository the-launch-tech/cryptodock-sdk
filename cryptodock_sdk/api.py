from .controllers import CoinbasePro, Kucoin, Local

class CryptoDockApi :

    def __init__(self, Args) :
        self.base = Args.API_HOST
        self.port = Args.API_PORT
        self.version = Args.API_VERSION
        self.uri = "http://{}:{}/api/{}".format(self.base, self.port, self.version)

        self.Local = Local(self.uri)
        self.Kucoin = Kucoin(self.uri)
        self.CoinbasePro = CoinbasePro(self.uri)
