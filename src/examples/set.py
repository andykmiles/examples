"""set program"""


# 1
def setComp():
    return {(integer, integer ** 2)
        for integer in range(1, 100001)
        if integer ** 2 % 3 == 0
    }


def minMaxSet(a_set):
    lowest = lowest_possible = float('inf') * -1
    highest = highest_possible = float('inf')
    for set_member in a_set:
        if lowest == lowest_possible or set_member < lowest:
            lowest = set_member
        if highest == highest_possible or set_member > highest:
            highest = set_member
    return lowest, highest


def uniqueElems(values):
    if len(values) == len(set(values)):
        return True
    return False


def commonElems(A, B):
    return frozenset(A ^ B)


def addsToK(A, k):
    for num in A:
        if k - num in A:
            return True
    return False


def answer_questions():
    q1 = setComp()
    # check boundaries
    assert (3, 9) in q1
    assert (99999, 99999 ** 2) in q1
    assert(10, 100) not in q1
    assert(0,0) not in q1

    q2 = minMaxSet({5, 7, 1, 8, 5, 9, 2})
    assert q2 == (1, 9)

    q3 = uniqueElems([3, 4, 5, 2, 5, 1])
    assert q3 == False
    q3 = uniqueElems([3, 4, 5, 2, 7, 1])
    assert q3 == True

    q4 = commonElems({5, 7, 2, 8, 4}, {99, 2, 7, 1})
    for _ in {1, 4, 5, 888, 99}:
        assert _ in q4

    q5 = addsToK({4, 7, 2, 11, 32, 5}, 11)
    assert q5 is True
    q5 = addsToK({4, 7, 2, 11, 32, 5}, 99)
    assert q5 is False


if __name__ == "__main__":
    answer_questions()
    print("done")
