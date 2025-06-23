import pytest
from logic import Finance_manager 

#This test for a valid category
def test_add_valid_category():
    manager= Finance_manager ()
    manager.add_category("Food")
    assert len(manager.get_categories())==1
    assert manager.get_categories()[0].name == "Food"


# Is not valid a empty category

def add_empty_category():
    manager = Finance_manager()
    with pytest.raises(ValueError) as e:
        manager.add_category("")
    assert str(e.value) == "Category name can not be empty"



#Category duplicate denied
def test_add_duplicate_category():
    manager= Finance_manager()
    manager.add_category("Food")
    with pytest.raises(ValueError) as e:
        manager.add_category("Food")
    assert str(e.value) == "Category already exist"



#Add_  an valid income
def test_add_valid_income():
    manager = Finance_manager()
    manager.add_category("Salary")
    manager.add_movement("Monthly salary",3000, "Salary", "income" )
    assert len(manager.get_movements())==1
    assert manager.get_movements()[0].model == "income"


#Empty title denied
def test_empty_title_movement():
    manager = Finance_manager()
    manager.add_category("Transport")
    with pytest.raises (ValueError) as e:
        manager.add_movement("",50, "Transport", "Expense")
    assert str(e.value)== "Title can not be empty"


#Negative amount or 0 denied 

def test_negative_amount():
    manager=Finance_manager()
    manager.add_category("Groceries")
    with pytest.raises (ValueError) as e:
        manager.add_movement("Fruits",0,"Groceries", "expense")
    assert str(e.value) == "Amount must be greater than 0"


#this category does not exist
def test_category_not_found():
    manager = Finance_manager()
    with pytest.raises(ValueError) as e:
        manager.add_movement("Taxi",10,"Travel","expense")
    assert str(e.value) == "Category does not exist"


#Incorrect model

def test_invalid_model():
    manager = Finance_manager()
    manager.add_category("Other")
    with pytest.raises(ValueError) as e:
        manager.add_movement("Gift", 100,"other", "bonus")
    assert str(e.value) == "Model must be income or expense"

#Deleted a movements that not exist
def test_delete_movement():
    manager=Finance_manager()
    manager.add_category("Work")
    manager.add_movement("Payment", 500, "work", "income")

    assert len(manager.get_movements()) == 1

    manager.delete_movement("Payment",500,"Work", "income")

    assert len(manager.get_movements())== 0



#Error from deleted movements doesnt exist
def test_delete_not_exist_movement():
    manager = Finance_manager()
    manager.add_category("Work")