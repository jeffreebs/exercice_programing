def bubble_sort_vocables(letters):
    if not isinstance(letters,list):
        raise TypeError("We waiting a list of letters")
    l=len(letters)
    for z in range(l):
        for x in range(0,l-z-1):
            if letters[x].lower() > letters[x+1].lower():
                letters[x],letters[x+1]= letters[x+1],letters[x]
    return letters


vocables= ["o","a","i","e","u"]
order = bubble_sort_vocables(vocables[:]) 
print("Resultado ordenado:", order)