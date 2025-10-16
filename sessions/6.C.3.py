import random
randarr = []
for i in range(0,50):
    randarr = randarr + [random.randint(1,100)]



for i in range(len(randarr)):
    for j in range(0, len(randarr)-1):
        if randarr[j] > randarr[j + 1]:
            # Swap elements
            randarr[j], randarr[j + 1] = randarr[j + 1], randarr[j]

print(randarr)
