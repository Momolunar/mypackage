def bubble_sort(items):
    '''
    Return array of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values or strings.

    Returns:
        array: array of items, in ascending order.

    Examples:
        >>> bubble_sort(['aa', 'xx', 'zz', 'bb', 'cc'])
        ['aa', 'bb', 'cc', 'xx', 'zz']

        >>> bubble_sort([10, 100, 5, 12, 55])
        [5, 10, 12, 55, 100]

    '''
    x=1
    while x:
        x = 0
        for i in range(1,len(items)):
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                x = 1
    return items

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values or strings.

    Returns:
        array: array of items, in ascending order.

    Examples:
        >>> merge_sort(['patch', 'tour', 'yak', 'zombie', 'egg', 'stall'])
        ['egg', 'patch', 'stall', 'tour', 'yak', 'zombie']

        >>> merge_sort([25, 1, 36, 100, 12, 5])
        [1, 5, 12, 25, 36, 100]

    '''
    def linear_merge(list1, list2):
        ### BEGIN SOLUTION
        merge_list = []
        idx1, idx2 = 0, 0
        while idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] < list2[idx2]:
                merge_list.append(list1[idx1])
                idx1 += 1
            elif list2[idx2] < list1[idx1]:
                merge_list.append(list2[idx2])
                idx2 += 1
        if len(list1) > idx1:
            merge_list += list1[idx1:]
        elif len(list2) > idx2:
            merge_list += list2[idx2:]
        ### END SOLUTION
        return merge_list

    if len(items)==1:
        return items

    mid_pnt = len(items)//2
    list1 = merge_sort(items[:mid_pnt])
    list2 = merge_sort(items[mid_pnt:])

    return linear_merge(list1,list2)

def quick_sort(items):
    '''
    Return array of items, sorted in ascending order
    Args:
        items (array): list or array-like object containing numerical values or strings.

    Returns:
        array: array of items, in ascending order.

    Examples:
        >>> quick_sort(['patch', 'tour', 'yak', 'zombie', 'egg', 'stall'])
        ['egg', 'patch', 'stall', 'tour', 'yak', 'zombie']

        >>> merge_sort([25, 1, 36, 100, 12, 5])
        [1, 5, 12, 25, 36, 100]
    '''
    
    if len(items)<=1:
        return items
    idx = 0
    left = []
    right = []
    pivot = []
    for i in range(len(items)):
        if items[i] < items[idx]:
            left.append(items[i])
        elif items[i] > items[idx]:
            right.append(items[i])
        elif items[i] == items[idx]:
            pivot.append(items[idx])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + pivot + right
    
    return sorted(items)
