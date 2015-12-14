def is_substring(s1, s2):
    if s1 in s2:
        return True
    return False

def is_rotation(s1, s2):
    return is_substring(s1, s2 + s2)

print "waterbottle", "bottlewater", is_rotation("waterbottle", "bottlewater")
print "water", "water", is_rotation("water", "water")
print "water", "wate", is_rotation("water", "wate")
print "empty strings", is_rotation("", "")
print "aioaf", "ioafa", is_rotation("aiodf", "ioafa")
