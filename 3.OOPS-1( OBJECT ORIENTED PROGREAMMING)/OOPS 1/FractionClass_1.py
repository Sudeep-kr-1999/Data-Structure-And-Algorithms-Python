# <<<<<<<<<<<<[ Building Fraction Class]>>>>>>>>>>>>>>>>>>

class Fraction:
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den

f=Fraction(2,3)
print(f.__dict__)
f1=Fraction()
print(f1.__dict__)
f2=Fraction(3)
print(f2.__dict__)
