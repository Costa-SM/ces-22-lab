import math

def is_prime(n):
    """
    :param n: possibly prime number. 
    :type n: int.
    :rtype: bool.
    """

    # the smallest prime number is 2
    # we check up to the sqrt of the number. Since the sqrt
    # is a float, we can use the ceiling function of the number
    # as the upper limit
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    
    return True

print(is_prime(2))
print(is_prime(7))
print(is_prime(97))
print(is_prime(15))
