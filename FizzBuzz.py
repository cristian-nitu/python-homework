start = 1
end = 100

for val in range(start, end+1):
    # If num is divisible by any number
    # between 2 and val, it is not prime
    if val > 1:
        for n in range(2, val):
            if (val % 15) == 0:
                print('fizzbuzz')
                break
            elif (val % 5) == 0:
                print('buzz')
                break
            elif (val % 3) == 0:
                print('fizz')
                break
        else:
            print(val)




