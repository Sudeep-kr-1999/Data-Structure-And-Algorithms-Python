# <<<<<<<<<<<<<[ FRACTION CLASS]>>>>>>>>>>>>

class Fraction:
    def __init__(self,num=0,den=1):
        if den==0:
            # throw error
            den=1

        self.num=num
        self.den=den
    def print(self):
        if self.num==0:
            print(0)
        elif self.den==1:
            print(self.num)
        else:
            print(self.num,"/",self.den)


    def simplify(self):
        if self.num==0:
            self.den=1
            return
        current=min(self.num,self.den)
        while current>1:
            if self.num % current==0 and self.den %current==0:
                break
            current-=1
        self.num=self.num//current
        self.den=self.den//current



# f=Fraction(2,3)
# f1=Fraction(0,3)
# f2=Fraction(2,1)
# f4=Fraction(14,5)
f5=Fraction(0,5)

# f.print()
# f1.print()
# f2.print()
# f4.print()
# f4.simplify()
# f4.print()

f5.print()
f5.simplify()
f5.print()
