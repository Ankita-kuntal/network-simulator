import random

def add_noise(data):
    if random.random() < 0.3:
        return data + " [NOISE]"
    return data