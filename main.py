def is_palindrome(n):
    """
    determina daca un numar este palindrom
    :param n: un numar intreg
    :return: True daca este palindrom sau False in caz contrar
    """
    cn=n
    oglindit=0
    while cn!=0:
        oglindit=cn%10+oglindit*10
        cn=cn//10
    if n==oglindit:
        return True
    return False

def test_is_palindrome():
    #assert (565) == True
    assert (567) == False

def is_prime(n):
    """
    determina daca un numar este prim
    :param n: ün numar intreg
    :return: True, daca n este prim, False in caz contrar
    """
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True

def is_superprime(n):
    """
    determina daca un numar este superprim
    :param n: un numar intreg
    :return: True, daca n este superprim sau False in caz contrar
    """
    while n!=0:
        if is_prime(n)!=True:
            return False
        n=n//10
    return True

def test_is_superprime():
    assert (73) == True
    assert (246) == False

shouldRun=True
while shouldRun:
    print('1. Determină dacă un număr dat este palindrom.')
    print('2. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.')
    optiune=input ('Dati optiunea:')
    if optiune == "1":
        n = int(input("Dati un numar:"))
        print(is_palindrome(n))
    elif optiune == "2":
        x = int(input("Dati un numar:"))
        print(is_superprime(x))
    elif optiune == "x":
        shouldRun = False
    else:
        print("optiune gresita!")



