def turn_to_english(n):
    names = dict()
    names[1] = "One"
    names[2] = "Two"
    names[3] = "Three"
    names[4] = "Four"
    names[5] = "Five"
    names[6] = "Six"
    names[7] = "Seven"
    names[8] = "Eight"
    names[9] = "Nine"
    names[10] = "Ten"
    names[11] = "Eleven"
    names[12] = "Twelve"
    names[13] = "Thirteen"
    names[14] = "Fourteen"
    names[15] = "Fifteen"
    names[16] = "Sixteen"
    names[17] = "Seventeen"
    names[18] = "Eighteen"
    names[19] = "Nineteen"
    names[20] = "Twenty"
    names[30] = "Thirty"
    names[40] = "Fourty"
    names[50] = "Fifty"
    names[60] = "Sixty"
    names[70] = "Seventy"
    names[80] = "Eighty"
    names[90] = "Ninety"
    names[100] = "Hundred"
    names[1000] = "Thousand"
    names[1000000] = "Million"

    translation = ""
    if n < 0:
        translation += "Negative "
        n *= -1
    elif n == 0:
        return "Zero"
    while n > 0:
	digits = len(str(n))
        if digits ==  1:
            translation += 

    return translation

def digits(n):
    digits = 0
    while n > 0:
        n /= 10
	digits += 1
    return digits

def main():
    for i in range(-9, 99):
        print turn_to_english(i)

main()
