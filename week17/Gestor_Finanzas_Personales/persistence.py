import json
import os

categories_files="data/categories.json"
movements_files = "data/movements.json"

def save_categories(categories):
    data = [{"name":cat_.name}for cat_ in categories]
    with open (categories_files,"w",encoding="utf-8")as f:
        json.dump(data,f,indent=4)


def load_categories():
    if not os.path.exists(categories_files):
        return[]
    

    with open(categories_files,"r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [cat_["name"] for cat_ in data]
        except json.JSONDecodeError:
            return[]
    

def load_movements():
    if not os.path.exists(movements_files):
        return[]
    

    with open(movements_files,"r", encoding="utf-8")as f:
        try:
            data=json.load(f)
            return data
        except json.JSONDecodeError:
            return[]


def save_movements(movements):
    data = []
    for mov in movements:
        data.append({
            "title":mov.title,
            "amount":mov.amount,
            "category":mov.category,
            "model":mov.model
        })


    with open (movements_files,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)
        