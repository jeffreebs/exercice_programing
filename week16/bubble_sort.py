def bubble_sort_last_name(LastName):
    l=len(LastName)
    for z in range(l):
        for x in range(0,l-z-1):
            if LastName[x].lower() > LastName[x+1].lower():
                LastName[x],LastName[x+1]= LastName[x+1],LastName[x]
    return LastName
    

last_name=["Zuñiga", "García","Berrocal", "Artavia"]
order= bubble_sort_last_name(last_name)
print("The last name ordered list are:",order)