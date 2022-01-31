import random

coin = [0, 1]  # 0 for head, 1 for tail

trials = 50000

for i in range(trials):
    toss = random.randint(0, 1)
    coin[toss] = coin[toss] + 1

print(f"Heads: {coin[0]}")
print(f"Tails: {coin[1]}")
