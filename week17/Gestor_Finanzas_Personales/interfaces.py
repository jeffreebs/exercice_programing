import FreeSimpleGUI as sg
import persistence

# from logic import Finance_manager
# import persistence



    


# manager = Finance_manager()

# for cat in persistence.load_categories():
#     try:
#         manager.add_category(cat)
#     except ValueError:
#         pass


# for mov in persistence.load_movements():
    
#     try:
#         manager.add_movement(mov["title"],mov["amount"],mov["category"],mov["model"])
#     except ValueError:
#         pass


#this is an function to refresh the table 
def run_interface(manager):
    def refresh_table():
        movements = manager.get_movements()
    
        if movements and any(mov.title.strip() for mov in movements):
            return [[
                mov.title,
                f"${mov.amount:.2f}", 
                mov.category, 
                mov.model
                ] for mov in movements]
        else:
            cats = manager.get_categories()
            return [["", "", cat.name if hasattr(cat, "name") else cat, ""] for cat in cats]


#principal layout

    layout= [
        [sg.Text("Personal Finance Manager", font=("Helvetica",16), justification='center', expand_x=True)],


        [sg.Table(
            headings=["Title", "Amount", "Category", "Model"],
            values=[],
            key="TABLE",
            auto_size_columns=False,
            justification="center",
            col_widths=[15, 10, 15, 10],
            expand_x=True,
            expand_y=True,
            vertical_scroll_only=False,
            enable_events=True,
            select_mode=sg.TABLE_SELECT_MODE_BROWSE
        )],
        [sg.Button("Add category", expand_x=True), 
        sg.Button("Add income",expand_x=True), 
        sg.Button("Add spent",expand_x=True), 
        sg.Button("Delete", expand_x=True),
        sg.Button("Refresh", expand_x=True), 
        sg.Button("Exit",expand_x=True),
        
        
        ]

]

    window = sg.Window("Finance Manager", layout, size=(800, 600), resizable=True, finalize=True)


    window["TABLE"].update(values=refresh_table())  # <--- ESTA LÍNEA




    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        elif event == "Add category":
            cat_event, cat_vals = sg.Window("New Category", [
                [sg.Text("Name of category:")],
                [sg.Input(key="NEW_CAT")],
                [sg.Button("Save"), sg.Button("Cancel")]
            ]).read(close=True)


        


            if cat_event == "Save":
                try:
                    manager.add_category(cat_vals["NEW_CAT"])
                    window["TABLE"].update(values=refresh_table())  
                except ValueError as e:
                    sg.popup_error(str(e))


        elif event == "Delete":
            selected = values["TABLE"]  

            if selected:
                index = selected[0]
                data = refresh_table() 


                if index < len(data):
                    row = data[index]
                    title = row[0].strip()
                    amount = row[1].strip().replace("$", "")
                    category = row[2].strip()
                    model = row[3].strip()

                    if title and amount and model:
                        try:
                            amount = float(amount)
                            manager.delete_movement(title, amount, category, model)
                            sg.popup("Movements deleted successfully.")
                        except ValueError:
                            sg.popup_error("Can not delete the movements.")
            
                    elif not title and not amount and not model and category:
                        try:
                            manager.delete_category(category)
                            sg.popup(f"Category '{category}' and yours deleted movements.")
                        except ValueError as e:
                            sg.popup_error(f"Can not delete the: {str(e)}")

                    window["TABLE"].update(values=refresh_table())
                else:
                    sg.popup_error(" Error to access to the queue selected , refresh the table")
            else:
                sg.popup_error("Please choose a queue before to delete.")


            

        elif event == "TABLE":
            pass  



        elif event == "Refresh":
            window["TABLE"].update(values=refresh_table())





        elif event in ("Add income","Add spent"):
            model = "income" if event == "Add income" else "expense"

            if not manager.get_categories():
                sg.popup_error("First you need to add the category")
                continue


        

            current_categories = [cat.name for cat in manager.get_categories()]

            layout_mov = [
                [sg.Text("title"), sg.Input(key="TITLE")],
                [sg.Text("amount"), sg.Input(key="AMOUNT")],
                [sg.Text("Category"), sg.Combo(current_categories, key="CATEGORY")],
                # [sg.Text("category"), sg.Combo(
                #     [cat.name for cat in manager.get_categories()],
                #     key="CATEGORY")],
                [sg.Button("Save"), sg.Button("Cancel")]


            ]

            mov_event, mov_vals = sg.Window("New movements", layout_mov).read(close=True)


            if mov_event == "Save":
                try: 
                    title = mov_vals["TITLE"]
                    amount = float(mov_vals["AMOUNT"])
                    category= mov_vals["CATEGORY"]

                    if not category:
                        sg.popup_error("Please select a category.")
                        continue

                    manager.add_movement(title,amount,category,model)
                    window["TABLE"].update(values=refresh_table())
                    # persistence.save_movements(manager.get_movements())

                except ValueError as e:
                    sg.popup_error(str(e))


    window["TABLE"].update(values=refresh_table())

    


    window.close()