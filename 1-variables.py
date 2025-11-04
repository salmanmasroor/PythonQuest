
#Swap Two numbers without using a temporary vaiable
def swap_number(a: int ,b: int) -> tuple[int,int]:  # concept of type hinting
    a = a + b
    b = a - b
    a = a - b
    return (a, b)


# Check if a variable is an integer, float, or string and perform different operations based on the type.
def check_variable(x: int| float | str) -> str :
    if isinstance(x, int):
        return f"{x} is integer"
    elif isinstance(x, float):
        return f"{x} is float"
    elif isinstance(x, str):
        return f"{x} is String"
    else:
        return "unknown"

# Convert a string containing a number to an integer and a float
def convert_string_no(str_value: str) -> tuple[tuple[int, str], tuple[float, str]]:
    integer = int(str_value)
    float_no = float(str_value)
    return (integer, str(type(integer))), (float_no, str(type(float_no)))

#  Find the largest and smallest numbers in a list.
def max_min_number(no_list: list) -> dict:
    maximum = no_list[0]
    minimum = no_list[0]
    for number in no_list:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    
    return {"max": maximum, "min": minimum}

# Count the number of occurrences of a value in a list.
def occurrences_of_number(no_list: list) -> dict:
    length = len(no_list)
    output = {}
    check = []
    for i in range(length):
        count = 0
        if(no_list[i] in check):
            continue
        check.append(no_list[i])

        for j in range(length):
            if(no_list[i] == no_list[j]):
                count += 1
        output[no_list[i]] = count
    
    return output

if __name__ == "__main__":

    print(swap_number(12,23)) 

    print(check_variable(12))

    print(convert_string_no("12"))

    numbers = [12,23,43,12,34,12]

    print(max_min_number(numbers))

    print(occurrences_of_number(numbers))

