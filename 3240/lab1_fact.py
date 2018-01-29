# Duncan Lee (ddl9be)
# Lab 101
# lab1_fact.py
# January 22, 2018

def factorial1(n):
    if n < 0:
        raise ValueError
    if (n == 0):
        return 1
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

def factorial2(n):
    array = []
    for i in range(0,n+1):
        array.append(factorial1(i))
    #print(array)
    return array

def test_fact1():
    #assert factorial1(-1) == "ValueError", "valueerror not working"
    assert factorial1(0) == 1, "n=0 not returning 1"
    assert factorial1(1) == 1, "n=1 not returning 1"
    assert factorial1(5) == 120, "n=5 not returning 120"

def test_fact2():
    assert factorial2(0) == [1], "n=0 not returning [1]"
    assert factorial2(1) == [1, 1], "n=1 not returning [1, 1]"
    assert factorial2(2) == [1, 1, 2], "n=2 is wrong"
    print(factorial2(-2))

if __name__ == "__main__":
    test_fact1()
    test_fact2()