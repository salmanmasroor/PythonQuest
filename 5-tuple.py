# tuple

# write a program to calculate the sum of all numbers.
def sum_all(val: str) -> int:
    sum  = 0
    for i in range(len(val)):
        if isinstance(val[i], int):
            sum+=val[i]
        else:
            for j in range(len(val[i])):
                sum += val[i][j]
    return sum

val_input = (1, (2, 3), 4, (5, 6))

print(sum_all(val_input))