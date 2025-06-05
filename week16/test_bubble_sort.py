from bubble_sort import bubble_sort_last_name

def test_bubble_sort_last_name_in_order():

#Arrange
    last_name=["Zamora", "García","Berrocal", "Artavia"]
    #Act
    order= bubble_sort_last_name(last_name)
    #Assert
    assert order == ["Artavia", "Berrocal", "García", "Zamora"]

