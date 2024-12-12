from Math_operation.Basic_operation import arithematic
from Math_operation.Geometry import area
print("Arithematic operation: ")
print("5+3= ",arithematic.add(5,3))
print("10-7= ",arithematic.substrat(10,7))
print("5*3= ",arithematic.mutiply(5,3))
print("8/2= ",arithematic.divide(8,2))
print("8/0= ",arithematic.divide(8,0))


#area calculation#

print("\n Area calculation" )
print("rectangle(length=5,width=3):",area.rectangle_area(5,3))
print("circle(radius=7):",area.circle_area(7))
print("triangle(base=4,height=5):",area.triangle_area(4,5))
