from recsort import recursion, sorting

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert myFunction.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myFunction.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myFunction.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'

def test_sum_array():
    '''
    make sure sum_array function works correctly
    '''

    assert recursion.sum_array([1,2,3,4,5]) == 15, 'incorrect'
    assert recursion.sum_array([10,2,1]) == 13, 'incorrect'
    assert recursion.sum_array([2]) == 2, 'incorrect'

def test_fibonnaci():
    '''
    make sure fibonacci function works correctly
    '''

    assert recursion.fibonacci(14) == 377, 'incorrect'
    assert recursion.fibonacci(0) == 0, 'incorrect'
    assert recursion.fibonacci(7) == 13, 'incorrect'

def test_factorial():
    '''
    make sure factorial function works correctly
    '''

    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(10) == 3628800, 'incorrect'
    assert recursion.factorial(3) == 6, 'incorrect'

def test_bubble_sort():
    '''
    make sure bubble_sort function works correctly
    '''

    assert sorting.bubble_sort([10, 100, 5, 12, 55]) == [5, 10, 12, 55, 100], 'incorrect'
    assert sorting.bubble_sort(['aa', 'xx', 'zz', 'bb', 'cc']) == ['aa', 'bb', 'cc', 'xx', 'zz'], 'incorrect'
    assert sorting.bubble_sort(['patch', 'tour', 'yak', 'zombie', 'egg', 'stall']) == ['egg', 'patch', 'stall', 'tour', 'yak', 'zombie'], 'incorrect'


def test_reverse():
    '''
    make sure reverse function works correctly
    '''
    assert sorting.reverse('hello') == 'olleh', 'incorrect'
    assert sorting.reverse('hello there') == 'ereht olleh', 'incorrect'
    assert sorting.reverse('A') == 'A', 'incorrect'

def test_merge_sort():
    '''
    make sure merge_sort function works correctly
    '''
    assert sorting.merge_sort([10, 100, 5, 12, 55]) == [5, 10, 12, 55, 100], 'incorrect'
    assert sorting.merge_sort(['aa', 'xx', 'zz', 'bb', 'cc']) == ['aa', 'bb', 'cc', 'xx', 'zz'], 'incorrect'
    assert sorting.merge_sort(['patch', 'tour', 'yak', 'zombie', 'egg', 'stall']) == ['egg', 'patch', 'stall', 'tour', 'yak', 'zombie'], 'incorrect'
