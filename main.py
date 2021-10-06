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
    assert (565) == True
    assert (567) == False

def is_prime(n):
    """
    determina daca un numar este prim
    :param n: Un numar intreg
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

def get_largest_prime_below(n):
    """
    gaseste ultimul număr prim mai mic decât un număr dat
    :param n: un numar intreg
    :return: ultimul număr prim mai mic decât un număr dat
    """
    for i in range(n-1, 2, -1):
        if is_prime(i)==True:
            return i
    print("Nu exista un astfel de numar")

def test_get_largest_prime_below():
    assert (3) == "Nu exista un astfel de numar"
    assert (32) == 31
    assert (10) == 7

def main():
    shouldRun = True
    while shouldRun:
        print("1. Determină dacă un număr dat este palindrom.")
        print("2. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
        print("3. Găsește ultimul număr prim mai mic decât un număr dat.")
        optiune = input("Dati optiunea:")
        if optiune == "1":
            n = int(input("Dati un numar:"))
            print(is_palindrome(n))
        elif optiune == "2":
            x = int(input("Dati un numar:"))
            print(is_superprime(x))
        elif optiune == "3":
            a = int(input("Dati un numar:"))
            print(get_largest_prime_below(a))
        elif optiune == "x":
            shouldRun = False
        else:
            print("optiune gresita!")
if __name__ == '__main__':
main()




