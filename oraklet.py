
import random

svar = ["ja, helt klart.", "absolut inte", "fråga igen imorgon", "det vill du inte veta"]

fråga = int(input("fråga oraklet: "))
2print("du frågade:", fråga)
print(random.choice(svar))