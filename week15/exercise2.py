def bubble_sort_num(list):
    l=len(list)
    for n in range (l):
        for x in range (l-1,n,-1):
            if list[x]<list[x-1]:
                list[x],list[n-1]=list[x-1],list[n]
    return list


num= [1,2,3,4,5]
sort=bubble_sort_num(num)
print(sort)