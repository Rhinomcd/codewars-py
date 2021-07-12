import math


def cakes(recipe, available):
    return math.floor(min([available.get(key, 0) / recipe[key] for key in recipe]))
