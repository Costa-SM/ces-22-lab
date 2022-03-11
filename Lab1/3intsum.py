
def sum_to(n):
    """
    :param n: sum upper limit
    :type n: int.
    :rtype: int.
    """
    
    sum = 0
    for i in range(n):
        # range starts on integer 0, so we shift the sum by one
        sum += i + 1
    
    return sum

print(sum_to(10))