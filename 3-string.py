# strings

def palindrome(input_str: str) -> bool:
    chars = list(input_str)  # Convert string to list
    start = 0
    end = len(chars) - 1

    while start < end:
        # Swap characters
        temp = chars[start]
        chars[start] = chars[end]
        chars[end] = temp

        start += 1
        end -= 1

    # Convert list back to string
    reversed_str = ''.join(chars)
    if(input_str == reversed_str):
        return True
    else:
        return False

def palindrome_v2(input_str: str) -> bool:
    return input_str == input_str[::-1]

def count_vowels(input_str: str) -> int:
    vowels = ['a','i','e','o','u']
    count = 0
    for i in range(len(input_str)):
        if input_str[i] in vowels:
            count +=1
    return count

def remove_duplicate(text: str) -> str:
    char = list(text)
    present = []
    for i in char:
        for j in char:
            if i == j:
                if i not in present:
                    present.append(i)
    new_string = "".join(present)
    return new_string

def remove_duplicate_v2(text: str) -> str:
    result = []
    for char in text:
        if char not in result:
            result.append(char)
    
    output = "".join(result)
    return output

print(remove_duplicate_v2("aabc"))