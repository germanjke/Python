class Calculations:
    """This class creater like a example of OOP in Python.
    And shows how works methods like str, int, float, bool and complex in class-game
    Enjoy!"""
    def __init__(self, nums):
        self.nums = list()
        for n in nums:
            self.nums.append(n)
    def __str__(self):
        txt = "Meaning of field-list:\n| "
        for n in self.nums:
            txt+=str(n) + " | "
        return txt
    def __int__(self):
        return len(self.nums)
    def __float__(self):
        avr = sum(self.nums)/int(self)
        return avr
    def __bool__(self):
        if int(self)%2==1:
            return True
        else:
            return False
    def __complex__(self):
        mn = min(self.nums)
        mx = max(self.nums)
        z = complex(mx,mn)
        return z
obj = Calculations({3.0, 7.5, 1.1, 4.4, 0.2})
print(Calculations.__doc__)
print(obj)
print("Elements in list: ", int(obj))
if obj:
    print("Odd length elements")
print("Average is: ", float(obj))
print("Minimum and maximum is: ", complex(obj))
