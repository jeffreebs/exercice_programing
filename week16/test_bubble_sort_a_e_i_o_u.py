
from bubble_sort_a_e_i_o_u import bubble_sort_vocables

def test_bubble_sort_vocables():
    #arrange
    vocables= ["o","a","i","e","u"]
    # vocables= {
    #     "A": "a"
    # }  
    #act
    order = bubble_sort_vocables(vocables[:])
    #assert
    assert order == ["a","e","i","o","u"]

    vocables= []
    order = bubble_sort_vocables(vocables[:])
    assert order == []



    vocables = ["u", "a", "e"]
    order = bubble_sort_vocables(vocables[:])
    assert order == ["a", "e", "u"]