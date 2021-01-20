import random

r_total = 0
for i in range(3):
    r = random.randint(1, 100)
    print(r, 'is the', i + 1, 'times producing numbers.')
    if i > 0 and i > i - 1:
        r_total += r
    else:
        a = r
total = r_total + a
print('Produced', i + 1, 'numbers in total.')
print('Total value:', total)
