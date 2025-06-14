from bubble_sort_year_num import bubble_sort_days

def test_bubble_sort_days():

    d=list(range(1,366))

    order= bubble_sort_days(d[:])

    assert order == list(range(1,366))


def test_bubble_sort_days_reverse():

    d = list(range(365, 0, -1))
    order = bubble_sort_days(d[:])
    assert order == list(range(1, 366))


def test_bubble_sort_days_random_sample():
    
    d = [5, 200, 50, 1, 365, 300]
    order = bubble_sort_days(d[:])
    assert order == [1, 5, 50, 200, 300, 365]