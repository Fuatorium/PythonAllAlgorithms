import random

def reservoir_sampling(stream, k):
    reservoir = []
    for i in range(k):
        reservoir.append(stream[i])
    for i in range(k, len(stream)):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir

if __name__ == "__main__":
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    print(f"Random {k} elements from stream: {reservoir_sampling(stream, k)}")
