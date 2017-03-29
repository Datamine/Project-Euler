#!/usr/bin/python3

def main():
    # write down all the unique mappings, then decompose numbers & take lengths.
    # the solution to this problem is kind of gross and not as elegant as the
    # others. this was a tedious problem and I tried to get it as quickly as possible.
    mappings = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
    }

    total = 0

    # deciding to use len() on everything rather than the obvious resultant number
    # so that this code is clearer

    for i in range(1,20):
        total += len(mappings[i])

    for j in range(20,1000):
        singles = j % 10
        tens = (j % 100) - singles
        hundreds_digit = ((j % 1000) - (tens + singles)) // 100

        # special case: when we've got something in range [11..19]
        if singles != 0 and tens!= 10:
            total += len(mappings[singles])
        if tens != 0:
            if tens == 10:
                total += len(mappings[tens + singles])
            else:
                total += len(mappings[tens])
        if hundreds_digit != 0:
            total += len(mappings[hundreds_digit])
            total += len(mappings[100])
            if singles != 0 or tens != 0:
                total += len("and")

    total += len("onethousand")
    return total

if __name__=='__main__':
	print(main())
