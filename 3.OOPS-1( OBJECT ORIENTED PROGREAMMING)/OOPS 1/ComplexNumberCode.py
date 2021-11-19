class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def plus(self,other):
        self.real = self.real+other.real
        self.imag = self.imag+other.imag
        C1.printComplex()

    def multiply(self,other):
        a = self.real*other.real + (-1*self.imag*other.imag)
        b = self.real*other.imag + self.imag*other.real
        self.real = a
        self.imag = b
        C1.printComplex()

    def printComplex(self):
        if self.imag>0:
        	print(self.real," + ","i",self.imag,sep="")
        else:
            print(self.real," - ","i",self.imag,sep="")



real,imag = [int(x) for x in input().strip().split(' ')]
C1 = ComplexNumber(real,imag)
real,imag = [int(x) for x in input().strip().split(' ')]
C2 = ComplexNumber(real,imag)
choice = int(input())
if choice==1:
    C1.plus(C2)
if choice==2:
    C1.multiply(C2)