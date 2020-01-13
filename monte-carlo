#The number of equal intervals divided by the sides of a single square
n = 500
#The price of division - the distance between the adjacent points
dz = 1/n
#The number of dots that get inside
dots = 0
#The initial value of the index that defines the point column
i = 0
#Cycle operator. Sort through the columns
for i in range(n+1):
#x - point coordinates
    x = dz*i
#The initial value of the second index that defines the point column
    j = 0
#The internal loop operator. We move the dots in one column
    for j in range(n+1):
#y - point coordinates
        y = dz*j
#Conditional operator, and adding points in case of satisfaction
        if y<=x and y>=x**2:
            dots += 1
#Increase the value of the second index per unit
        j += 1
#Increase the value of the first index per unit
    i += 1
#Calculate the area of the figure
area = dots/(n+1)**2
#Show the result
print("Area of figure:" , area)