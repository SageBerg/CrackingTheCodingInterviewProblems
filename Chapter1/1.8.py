def is_rotation(string1, string2):

    if len(string1) != len(string2):
        return False
    if len(string1) == 0:
        return True

    target = string1[0]
    for i in range(len(string2)):
        if string2[i] == target:
            j = i
            iter_count = 0
            while iter_count < len(string1):
                if string1[iter_count] != string2[j]:
                    break
                j += 1
                j = j % len(string2)          
                iter_count += 1
            if iter_count == len(string2):            
		return True
    return False

def is_rotation_alt(string1, string2):

    if len(string1) != len(string2):
        return False
    if len(string1) == 0:
        return True 

    for _ in range(len(string1)):
        if string1 == string2:
            return True
        string1 = string1[-1] + string1[0:-1]
    return False

print "waterbottle", "bottlewater", is_rotation("waterbottle", "bottlewater")
print "water", "water", is_rotation("water", "water")
print "water", "wate", is_rotation("water", "wate")
print "empty strings", is_rotation("", "")
print "aioaf", "ioafa", is_rotation("aiodf", "ioafa")
print 
print "waterbottle", "bottlewater", is_rotation_alt("waterbottle", "bottlewater")
print "water", "water", is_rotation_alt("water", "water")
print "water", "wate", is_rotation_alt("water", "wate")
print "empty strings", is_rotation_alt("", "")
print "aioaf", "ioafa", is_rotation_alt("aiodf", "ioafa")
