def bubble_sort_num(list):
    l=len(list)
    for n in range (l):
        for x in range (0,l-n-1):
            if list[x]>list[x+1]:
                list[x],list[x+1]=list[x+1],list[x]
    return list


num= [1,2,3,4,5]
sort=bubble_sort_num(num)
print(sort)





