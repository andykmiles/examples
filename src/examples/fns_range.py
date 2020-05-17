# 1


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(2))
print(is_even(1))

allEven = list(filter(is_even, range(3, 1000, 3)))
print(allEven)
# OR

allEven = list(filter(lambda n: n % 2 == 0, range(3, 1000, 3)))


# 2


def is_prime(num):
    return not any(num % i == 0 for i in range(2, num))


primes = []
candidate_num = 1
while True:
    if is_prime(candidate_num):
        primes.append(candidate_num)
        if len(primes) == 10:
            break
    candidate_num += 1

print(primes)

# 3


def firstLast(numbers):
    return [numbers[0], numbers[-1]]


print(firstLast([3, 4, 5, 99, 1]))

# 4


def listSum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(listSum([11, 12, 2]))

# 5
def commonElems(first, second):
    return [item for item in first if item in second]


print(commonElems([1, 2, 3, 4, 5], [2, 4, 7]))

# 6
def uniqueElems(items):
    return list(set(items))


print(uniqueElems([1, 2, 2, 3, 2, 4, 8, 3, 6, 8]))

# 7
def sortList(items):
    n = 0
    while n < len(items):
        smallest = min(items[n:])
        index_of_smallest = items.index(smallest)
        items[n], items[index_of_smallest] = items[index_of_smallest], items[n]
        n += 1
    return items


print(sortList([6, 2, 7, 3, 77, 1, 0]))

# 8


def rotateList(a, k):
    return a[k:] + a[:k]


print(rotateList([1, 4, 7, 13, 9], 2))
