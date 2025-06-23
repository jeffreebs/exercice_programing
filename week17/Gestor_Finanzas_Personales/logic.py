class Category:
    def __init__(self,name):
        self.name = name

class Movement:
    def __init__(self,title,amount, category, model):
        self.title = title
        self.amount=amount
        self.category = category
        self.model = model


class Finance_manager:
    def __init__(self):
        self.categories = []
        self.movements = []


    def add_category(self,name_category):
        #Validation to not repeat a category and empty
        if not name_category.strip():
            raise ValueError ("Category name cannot be empty.")
        

        #validation for category with the same name

        for category in self.categories:
            if category.name.lower() == name_category.lower():
                raise ValueError ("Category already exist")
            

        new_category = Category(name_category)
        self.categories.append(new_category)


    def add_movement(self, title, amount,category, model):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        
        #Validation: the amount need to be a positive
        if amount <= 0:
            raise ValueError ("Amount must be greater than 0.")
        
        #Validation to know if some category is already exist
        if category not in [cat_.name for cat_ in self.categories]:
            raise ValueError("Category does not exist")
        
        #Validation to the model, need to be income or expense
        if model not in ("income", "expense"):
            raise ValueError ("Model must be  'income' or ' expense' ")
        


        new_movement=Movement(title,amount,category,model)
        self.movements.append(new_movement)


    def get_categories(self):
        return self.categories


    def get_movements(self):
        return self.movements
    

    def delete_movement(self, title, amount, category, model):
        for mov in self.movements:
            if (
                mov.title == title and
                mov.amount == amount and
                mov.category == category and
                mov.model == model
            ):
                self.movements.remove(mov)
                return
        raise ValueError("Movements can not find.")
    


    def delete_category(self, name_category):
        self.movements = [
            mov for mov in self.movements if mov.category != name_category
        ]

        for cat in self.categories:
            if cat.name == name_category:
                self.categories.remove(cat)
                return
        raise ValueError("Category can not find.")

