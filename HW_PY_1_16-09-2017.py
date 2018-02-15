class fraction:
    def __init__(self,numer, denom):
        self.numerator = numer
        if denom != 0:
            self.denominator = denom
        else:
            self.denominator = 1

    def change_num(self,numer):
        self.numerator = numer


    def change_den(self,denom):
        if denom != 0:
            self.denominator = denom
        else:
            self.denominator = 1

    def plus(self, number):
        return (self.numerator/self.denominator)+(number.numerator/number.denominator)

    def minus(self, number):
        return (self.numerator / self.denominator) - (number.numerator / number.denominator)

    def division(self, number):
        return (self.numerator / self.denominator) / (number.numerator / number.denominator)

    def  multiplication(self, number):
        return (self.numerator / self.denominator) * (number.numerator / number.denominator)

exampl1 = fraction(4,7)
print(exampl1.numerator, '/',exampl1.denominator )
exampl2 = fraction(3,8)
print(exampl2.numerator, '/',exampl2.denominator )
result = exampl1.plus(exampl2)
print(result)
result = exampl1.minus(exampl2)
print(result)
result = exampl1.division(exampl2)
print(result)
exampl2.change_num(6)
exampl2.change_den(7)
print(exampl2.numerator, '/',exampl2.denominator )
result = exampl1.multiplication(exampl2)
print(result)