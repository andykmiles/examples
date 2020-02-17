"""
performance analysis
"""
import sys
import csv
#sys.setrecursionlimit(1000)

class Memoize:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]


#@Memoize
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def save_it(alist, name):
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(alist)

def calc(write=False, ranges=(35, 30, 25, 40)):
    write = True
    a = [fibo(i) for i in range(ranges[0])]
    if write:
        save_it(a, 'a.csv')
    b = [fibo(i) for i in range(ranges[1])]
    if write:
        save_it(b, 'b.csv')
    c = [fibo(i) for i in range(ranges[2])]
    if write:
        save_it(c, 'c.csv')
    d = [fibo(i) for i in range(ranges[3])]
    if write:
        save_it(d, 'd.csv')

if __name__ == "__main__":
        calc()