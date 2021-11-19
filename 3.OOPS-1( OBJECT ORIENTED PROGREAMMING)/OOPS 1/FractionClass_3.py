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

    def add(self,otherFraction):
        newNum=otherFraction.den*self.num+otherFraction.num*self.den
        newDen=self.den*otherFraction.den
        self.num=newNum
        self.den=newDen
        self.simplify()

    def multiply(self,otherFraction):
        newNum=self.num*otherFraction.num
        newDen=self.den*otherFraction.den
        self.num=newNum
        self.den=newDen
        self.simplify()

f1=Fraction(4,6)
f1.print()
f2=Fraction(7,8)
f2.print()
# f1.add(f2)
# f1.print()
f1.multiply(f2)
f1.print()

