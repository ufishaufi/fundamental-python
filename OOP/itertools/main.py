from itertools import count
from itertools import accumulate, takewhile

for i in count(3):
    print(i, end=' ')

    if i >= 20:
        break

print()

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))