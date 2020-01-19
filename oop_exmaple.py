#This programm shows how Python OOP works. Exactly Claases
#Exactly this proggram will score 1st, 2nd, 3rd element and avarage of 4th and 5th
class Sum:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def sum(self):
        return self.A + self.B + self.C
    def show(self):
        print('Your objects:')
        print('A: ', self.A)
        print('B: ', self.B)
        print('C: ', self.C)
        print('Sum is ', self.sum())
class Average:
    def __init__(self, D, E):
        self.D = D
        self.E = E
    def ave(self):
        return int(((self.D * self.E) / 2))
    def show(self):
        print('Your objects:')
        print('D: ', self.D)
        print('E: ', self.E)
        print ('Average is ', self.ave())
class Score(Sum, Average):
    def __init__(self, A, B, C, D, E):
        Sum.__init__(self, A, B, C)
        Average.__init__(self, D, E)
        self.show()
    def show(self):
        Sum.show(self)
        Average.show(self)
obj=Score(1,2,3,4,5)


