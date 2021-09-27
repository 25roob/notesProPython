def isPrime(number: int) -> bool:
    """
    Function that applyes the Wilson's Theorem 
    to determine if a number is prime.
    """
    factorial = number -1
    for i in range(2, number-1):
        factorial *= i
    
    return (factorial + 1) % number == 0


def run():
    print(isPrime(-19))


if __name__ == '__main__':
    run()