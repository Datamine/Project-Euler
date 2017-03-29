#!/usr/bin/python3

def main():
    largest_pandigital = ""
    # we only need to check numbers up to 10,000. concatenating two five-digit
    # numbers would yield a number of length ten.
    for i in range(1, 10000):
        concatenated = ""
        for j in range(1, 10):
            concatenated += str(i*j)
            if "0" in concatenated or len(set(concatenated)) != len(concatenated):
                break
            if len(set(concatenated)) == 9:
                if concatenated > largest_pandigital:
                    largest_pandigital = concatenated

    return largest_pandigital

if __name__=='__main__':
    print(main())
