#!/usr/bin/python3

def main():
    products = set([])
    for i in range(1,100001):
        for j in range(i, 100001):
            combined = str(i*j) + str(i) + str(j)
            if len(combined) > 9:
                # future strings will only be longer
                break
            if "0" in combined or len(set(combined)) != 9:
                continue
            products.add(i * j)
    return sum(products)

if __name__=='__main__':
    print(main())
