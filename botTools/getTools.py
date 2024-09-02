from botTools.botSpecificTools.WhatsInScience import getWhatsInScienceData
from botTools.crypto.coinmarketcap import get_top_10_cryptocurrencies

#Data structure to return
# {
#     dataToUse: ...,
#     link: ...,
#     image:...
# }

def getDataFromTool(botName):
    returnData = {
        "dataToUse": None, 
        "link": None,
        "imageUrl": None
    }
    match botName:
        case 'CryptoSlave':
            returnData['dataToUse'] = get_top_10_cryptocurrencies()
        case 'WhatsInScience':
            returnData['dataToUse'] = getWhatsInScienceData()
    if returnData['dataToUse']:
        return returnData;
    return