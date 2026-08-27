
import random

svar = ["ja, helt klart.", "absolut inte", "fråga igen imorgon", "det vill du inte veta"]

fråga = (input("fråga oraklet: "))
print("du frågade:", fråga)
print(random.choice(svar))