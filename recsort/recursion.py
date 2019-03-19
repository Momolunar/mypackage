def sum_array(array):
    '''
    Return sum of all items in array

    Args:
        array (array): list or array-like object containing numerical values.

    Returns:
        int: sum of items.

    Examples:
        >>> sum_array([1,2,3,4,5])
        15
        '''
    if len(array)==1: #if one item in list, return the item
        return array[len(array)-1]
    else:
        return array[len(array)-1]+sum_array(array[:len(array)-1])

def fibonacci(n):
    '''
    Return nth term in fibonnaci sequence

    Args:
        n (int): positive integer n

    Returns:
        int: nth number in fibonacci sequence

    Examples:
        >>> fibonacci(14)
        377
        >>> fibonacci(7)
        13
    '''

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''
    Return factorial n

    Args:
        n (int): positive integer n

    Returns:
        int: nth factorial

    Examples:
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800

    '''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    '''
    Return word in reverse

    Args:
        word (str): string characters to be reversed

    Returns:
        str: reversed string

    Examples:
        >>> reverse('hello')
        'olleh'
        >>> reverse('hello there')
        'ereht olleh'

    '''
    if len(word)==1:
        return(word)
    else:
        return word[-1] + reverse(word[:-1])
