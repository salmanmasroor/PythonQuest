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


print(palindrome("aba"))  # Output: cba
