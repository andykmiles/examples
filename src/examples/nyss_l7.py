def setComp():
    ints = {int for int in range(1,10000)}
    squares = {int**2 for int in range(1,10000)}
    ints = sorted(ints)
    squares = sorted(squares)
    square_List = []
    nummies_List = []
    for nummybois in squares:
        if nummybois % 3 == 0:
            square_List.append(nummybois)
    for nummies in ints:
        if nummies % 3 == 0:
            nummies_List.append(nummies)
    comb_Ints_Squares = tuple(zip(nummies_List,square_List))
    return set({comb_Ints_Squares})
#set_Comp()

#HW_7_Question_2
def minMaxSet(x):
    sorted_X = sorted(x)
    minimum = sorted_X[0]
    maximum = sorted_X[-1]
    print({minimum, maximum})
    return {minimum, maximum}
#min_Max_Set({54, 65, 9, 1, 30, 4})

#HW_7_Question_3
def unique_Elems(elem_List):
    return set(elem_List)
unique_Elems([43, 12, 75, 33, 8, 12, 43, 2, 8])

#HW_7_Question_4
def common_Elems(A,B):
    A^=B
    return frozenset(A)
common_Elems({2, 8, 12, 33, 43, 75}, {45, 2, 90, 43, 16, 1})

#HW_7_Question_5
"""
q1 = setComp()
# check boundaries
assert (3, 9) in q1
assert (99999, 99999 ** 2) in q1
assert(10, 100) not in q1
assert(0,0) not in q1
"""
q2 = minMaxSet({5, 7, 1, 8, 5, 9, 2})
assert q2 == (1, 9)
"""
q3 = uniqueElems([3, 4, 5, 2, 5, 1])
assert q3 == False
q3 = uniqueElems([3, 4, 5, 2, 7, 1])
assert q3 == True

q4 = commonElems({5, 7, 2, 8, 4}, {99, 2, 7, 1})
for _ in {1, 4, 5, 8, 99}:
    assert _ in q4

q5 = addsToK({4, 7, 2, 11, 32, 5}, 11)
assert q5 is True
q5 = addsToK({4, 7, 2, 11, 32, 5}, 99)
assert q5 is False
"""
