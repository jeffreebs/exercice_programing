from bubble_sort import bubble_sort_last_name

def test_bubble_sort_last_name_empty_list():
    #arrange
    last_name=[]
    #act
    order= bubble_sort_last_name(last_name)
    #assert
    assert order == []