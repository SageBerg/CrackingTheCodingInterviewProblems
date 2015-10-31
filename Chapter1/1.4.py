def replace_spaces(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == " ":
            new_string += "%20"
        else:
            new_string += string[i]
    return new_string

print(replace_spaces("Mr. Jones is back in town."))
print(replace_spaces(""))
print(replace_spaces("   "))
