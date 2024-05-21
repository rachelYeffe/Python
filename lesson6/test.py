import pytest

list=[]
def count_primes(num):
    list=[]
    for n in range(2,num+1):
        prime=True
        for i in range(2,n):
            if(n%i == 0):
                prime=False
        if prime:
            list.append(n)
    return list
print(list)

def test_primes1():
    assert count_primes(13)==[2, 3, 5, 7, 11, 13]
@pytest.mark.importent
def test_primes2():
    assert count_primes(2)==[2]

