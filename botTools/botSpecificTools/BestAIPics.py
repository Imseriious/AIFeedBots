import random
from botTools.AIGeneratedImages.CivitAI import getCivitAiImages


def getPopularCivitAIPic():
    top10PopularToday = getCivitAiImages();
    random_image = random.choice(top10PopularToday)
    return random_image
