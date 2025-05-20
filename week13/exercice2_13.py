def numbers(func):
    def verification(a,b):
        try:
            num1 = float(a)
            num2 = float(b)
        except:
            raise ValueError ("All inputs needs to be a numbers o converted to numbers")
        

        return func(num1,num2)
    return verification


@numbers
def division(a,b):
    return a/b

print (division(10,2))
print(division(10,2.5))
print(division("Cars", 10))