#!/usr/bin/python3

def main():
    sequence = set([])
    for a in range(2,101):
        for b in range(2,101):
            sequence.add(a**b)
    return len(sequence)

if __name__=='__main__':
    print(main())
