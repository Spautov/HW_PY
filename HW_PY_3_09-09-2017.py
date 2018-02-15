small_number = 0
increase = 1
lim = 1
divis = 2*3*5*7*11*13*17*19

for i in range(1, 21):
    lim *= i

for small_number in range(divis,lim,divis):
    increase = 0
    for j in range(2, 21,):
        if (small_number % j != 0):
            increase += 1
    if (increase == 0):
        print('the smallest number that can be divided by each of the numbers')
        print('from 1 to 10 without any remainder is ', small_number)
        break
            

