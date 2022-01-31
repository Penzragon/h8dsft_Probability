import random

coin = [0, 1]  # 0 for head, 1 for tail

trials = 50000

for i in range(trials):
    toss = random.randint(0, 1)
    coin[toss] = coin[toss] + 1

print(
    f"Heads appear {coin[0]} times with probability of {round(coin[0]/trials * 100, 2)}%."
)
print(
    f"Tails appear {coin[1]} times with probability of {round(coin[1]/trials * 100, 2)}%."
)
