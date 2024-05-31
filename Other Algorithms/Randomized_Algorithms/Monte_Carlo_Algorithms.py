import random

def monte_carlo_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside_circle += 1
    return 4 * inside_circle / n

if __name__ == "__main__":
    n = 1000000
    print(f"Estimated value of Pi: {monte_carlo_pi(n)}")
