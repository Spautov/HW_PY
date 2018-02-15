max_polind = 0
number1 = 0
number2 = 0
k = 0
direct_str = ' '
inverse_str = ' '


for i in range(1000, 100,-1):
    for j in range(i, 100, -1):
        k = i*j
        direct_str = str(k)
        inverse_str = direct_str[::-1]
        direct_str = int(direct_str)
        inverse_str = int(inverse_str)
        if (direct_str == inverse_str)and (direct_str > max_polind):
            max_polind = direct_str
            number1 = i
            number2 = j

print('The largest palindrome made from the product of two 3-digit numbers is ')
print( max_polind, ' = ', number1, ' * ',number2)            

