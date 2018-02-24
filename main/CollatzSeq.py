print('Collatz Sequence Analyzer')

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return  3 * number + 1

def getInput():
    print('Enter Number: ')

    try:
        number = int(input())
        while number != 1:
            number = collatz(number)

        print("\n@Last 1 being reached")

    except ValueError:
        print('Error: Invalid argument.')
        getInput()

getInput()

'''
Output:
Collatz Sequence Analyzer
Enter Number: 
non integer
Error: Invalid argument.
Enter Number: 
3
10
5
16
8
4
2
1

@Last 1 being reached
'''