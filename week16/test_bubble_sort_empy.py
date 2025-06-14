from bubble_sort import bubble_sort_last_name

def test_bubble_sort_last_name_empty_list():
    #arrange
    last_name=[]
    #act
    order= bubble_sort_last_name(last_name)
    #assert
    assert order == []


def test_bubble_sort_last_name_single_element():

    last_name = ["Zamora"]
    order = bubble_sort_last_name(last_name)
    assert order == ["Zamora"]



def test_bubble_sort_last_name_multiple_elements():


    last_name = ["Lopez", "Alvarez", "Martinez", "Castro"]
    order = bubble_sort_last_name(last_name)
    assert order == ["Alvarez", "Castro", "Lopez", "Martinez"]