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

print(count_vowels("eulogia"))