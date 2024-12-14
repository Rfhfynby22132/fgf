import random


pass_1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lept = int(input("Ведите длину пороля"))
parole = []
for i in range(lept):
    parole+= random.choice(pass_1)
print(parole)
