from math import sqrt
class LinearEquationWarning(Warning):
    def __init__(self, b, c):
        try:
            self.x=-c/b
        except ZeroDivisionError:
            if c==0:
                self.x="any number"
            else:
                self.x="no solutions"
    def __str__(self):
        txt="Equation solutions: "
        txt+=str(self.x)
        return txt
class ComplexRootsError(Exception):
    def __init__(self, a,b,D):
        self.x1=complex(-b/2/a, sqrt(-D)/2/a)
        self.x2=complex(-b/2/a, -sqrt(-D)/2/a)
    def __str__(self):
        txt="x1 =" +str(self.x1) +"\n"
        txt+="x2 =" +str(self.x2)
        return txt
def show_params(a,b,c):
    print("Params: a={0}, b={1}, c={2}:".format(a,b,c))
def find_roots(a,b,c):
    show_params(a,b,c)
    try:
        if a==0:
            raise LinearEquationWarning(b,c)
        D=b*b-4*a*c
        if D<0:
            raise ComplexRootsError(a,b,D)
        x1=(-b+sqrt(D))/2/a
        x2=(-b-sqrt(D))/2/a
        print("x1 =", x1)
        print("x2 =", x2)
    except LinearEquationWarning as err:
        print("It's a linear equation")
        print(err)
    except ComplexRootsError as err:
        print("Solutions are complex!")
        print(err)
print("Solve the equation: a*x**2+b*x+c=0.")
find_roots(2,-3,1)
find_roots(1,2,1)
find_roots(0,-6,5)
find_roots(0,0,1)
find_roots(2,1,3)