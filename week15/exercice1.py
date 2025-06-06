def bubble_sort_num(list1):
    l=len(list1)
    for n in range (l):
        swapped= False


        for x in range (0,l-n-1):
            if list[x]>list[x+1]:
                list[x],list[x+1]=list[x+1],list[x]
                swapped= True


        if not swapped:
            break
    return list1


num= [1,2,3,4,5]
sort=bubble_sort_num(num)
print(sort)





