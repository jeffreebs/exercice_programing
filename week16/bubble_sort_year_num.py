def bubble_sort_days(numbers):
    l=len(numbers)
    for z in range(l):
        for x in range(0,l-z-1):
            if numbers[x] > numbers[x+1]:
                numbers[x],numbers[x+1]= numbers[x+1],numbers[x]
    return numbers
    
import random
d=list(range(1,366))
random.shuffle(d)
order= bubble_sort_days(d[:])
print("There are crazy list:",d)
print("The last name ordered list are:",order)