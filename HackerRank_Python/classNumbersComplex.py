#Herencia
class Complex(object):
    #Constructor
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    #Metodos
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    def __mul__(self, no):
        real=self.real*no.real - self.imaginary*no.imaginary
        imaginary=self.real*no.imaginary+self.imaginary*no.real
        return Complex(real,imaginary)
    def __truediv__(self, no):
        sr,si,orx,oi=self.real,self.imaginary,no.real,no.imaginary
        r=float(pow(orx,2)+pow(oi,2))
        totalreal=sr*orx+si*oi
        totalimag=si*orx-sr*oi
        return Complex(totalreal/r,totalimag/r)
    def mod(self):
        modulos=math.sqrt(pow(self.real,2)+pow(self.imaginary,2))
        return Complex(modulos,0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__=='__main__':
    numbers1=input().split()
    numbers2=input().split()
    real=numbers1[0]
    imaginary=numbers1[1]
    real2=numbers2[0]
    imaginary2=numbers2[1]
    numberComplex=Complex(real,imaginary)
    numberComplex2=Complex(real2,imaginary2)
    #to print of results 1 
    #to print of resuxlts 2