__author__ = 'saurabh'

def makeMyString(n):
    if(n == 1):
        return "A"
    else:

        tempString = "(" + makeMyString(n/2) + ")"

        if(n & 1):
            return tempString + "A"
        else:
            return tempString

def main():
    cases = input()
    while cases:
        number = input()
        s = makeMyString(number)
        print s
        cases -= 1

if(__name__ == "__main__"):
    main()