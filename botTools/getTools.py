from botTools.crypto.coinmarketcap import get_top_10_cryptocurrencies


def getDataForBot(botName):
    match botName:
        case 'CryptoSlave':
            return get_top_10_cryptocurrencies()
    return