
def return_the_numbers(number = [10,20,30,40,50]):
    sumatory = sum(number)
    print (f"The sum of the list is: {sumatory} ")
    number = [10,20,30,40,50]


def return_the_sum_of_list(number = [10,20,30,40,50]):
    return sum(number)


if __name__ == "__main__":
    return_the_numbers()