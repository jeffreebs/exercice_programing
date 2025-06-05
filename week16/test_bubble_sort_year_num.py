from bubble_sort_year_num import bubble_sort_days

def test_bubble_sort_days():

    d=list(range(1,366))

    order= bubble_sort_days(d[:])

    assert order == list(range(1,366))