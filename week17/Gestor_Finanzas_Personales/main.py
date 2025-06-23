from logic import Finance_manager
import persistence
from interfaces import run_interface



manager= Finance_manager()


# loaded_categories = persistence.load_categories()
for cat_name in persistence.load_categories():
    try:
        manager.add_category(cat_name)
    except ValueError:
        pass



# loaded_movements = persistence.load_movements()
for mov in persistence.load_movements():
    try:
        manager.add_movement(mov["title"],mov["amount"], mov["category"],mov["model"])
    except ValueError:
        pass


# try: 
#     manager.add_category("Food")
#     manager.add_category("Transport")
#     manager.add_category("Entertainment")
# except ValueError as e:
#     print("Error",e)



# print ("Categories:")
# for cat_ in manager.get_categories():
#     print("-",cat_.name)



# try:
#     manager.add_movement("Salary",2000,"Entertainment", "income")
#     manager.add_movement("Groceries",150,"Food","expense")
#     manager.add_movement("Bus ticket",20, "Transport", "expense")
# except ValueError as e:
#     print("Error",e)


# print("Movements:")
# for mov in manager.get_movements():
#     print (f" - {mov.title}: {mov.amount} ({mov.category})  [{mov.model}] ")

run_interface(manager)


persistence.save_categories(manager.get_categories())
persistence.save_movements(manager.get_movements())