import math

print('Fibonacci Sequence: The "nth" Term\n')
n = input('Enter term in its integer form: ')

if int(n) > 0:
    while True:
        try:
            val = int(n)
            result = round((1.618034 ** val - (1-1.618034)**6)/math.sqrt(5))
            print('The '+str(n)+'th term is: ' + str(result))
            break;
        except ValueError:
            try:
                float(n)
                print('Error: '+n+' is not valid input\n Please provide input in INTEGER form\n')
                break;
            except ValueError:
                print('Error: '+n+' is not valid input\n Please provide input in INTEGER form\n')
else:
    print('Error: There is no ' + n + 'th number in the sequence\n Please provide a valid input\n')
