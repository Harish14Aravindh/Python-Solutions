def sum_uppercase_ascii(text):
    total = 0
    for char in text:
        #ASCII values for the capitals between 'A' (65) and 'Z' (90)
        if 65 <= ord(char) <= 90:
            total += ord(char)
    return total

print(sum_uppercase_ascii("PyThOn"))
