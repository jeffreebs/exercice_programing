from bubble_sort import bubble_sort_last_name

def test_bubble_sort_last_name_in_order():

#Arrange
    last_name=["Zamora", "García","Berrocal", "Artavia"]
    #Act
    order= bubble_sort_last_name(last_name)
    #Assert
    assert order == ["Artavia", "Berrocal", "García", "Zamora"]



def test_bubble_sort_last_name_empty():

    last_name = []
    order = bubble_sort_last_name(last_name)
    assert order == []


def test_bubble_sort_last_name_single_element():
    
    last_name = ["Solano"]
    order = bubble_sort_last_name(last_name)
    assert order == ["Solano"]