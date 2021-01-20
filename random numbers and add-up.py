import random

r_total = 0
for i in range(3):
    r = random.randint(1, 100)
    print(i + 1, 'times produce:', r)
    if i >= i - 1:
        r_total += r
print('Produced', i + 1, 'numbers.')
print('Total value:', r_total)
