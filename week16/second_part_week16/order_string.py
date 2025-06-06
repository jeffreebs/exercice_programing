def order_strings(string):
    string_list = string.split("-")

    string_list_order = sorted(string_list)

    result = "-".join(string_list_order)

    return result


if __name__=="__main__":
    input_string = input("Enter some words to order the list: ")
    output_strings= order_strings(input_string)

    print(output_strings)