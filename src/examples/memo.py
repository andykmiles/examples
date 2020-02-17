"""
Memoization is a specific type of caching that is used as a software optimization technique.

A cache stores the results of an operation for later use. For example, your web browser will most likely use a cache to load this tutorial web page faster if you visit it again in the future.

So, when I talk about memoization and Python, I am talking about remembering or caching a function’s output based on its inputs. Memoization finds its root word in “memorandum”, which means “to be remembered.”

Memoization allows you to optimize a Python function by caching its output based on the parameters you supply to it. Once you memoize a function, it will only compute its output once for each set of parameters you call it with. Every call after the first will be quickly retrieved from a cache.

The basic memoization algorithm looks as follows:

- Set up a cache data structure for function results
- Every time the function is called, do one of the following:
- Return the cached result, if any; or
- Call the function to compute the missing result, 
  and then update the cache before returning the result to the caller

"""

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            print(f"memoizing {args}")
            self.memo[args] = self.fn(*args)
        else:
            print(f"not memoizing {args} - done already")
        return self.memo[args]


@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    fib(10)
    fib(20)
    fib(10)

if __name__ == "__main__":
    main()
# Work though https://dbader.org/blog/python-memoization

# References:
# https://www.marcelbelmont.com/post/caching-and-memoization/
# https://github.com/mikeboers/PyMemoize
