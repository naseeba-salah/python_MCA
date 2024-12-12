from Package.graphics.rectangle import rectangle_area,rectangle_perimeter
from Package.graphics.circle import circle_area, circle_perimeter

from Package.graphics.three_d.cuboid import cuboid_tsa,cuboid_volume
from Package.graphics.three_d.sphere import sphere_tsa, sphere_volume


print("Rectangle Area:", rectangle_area(5, 3))
print("Rectangle Perimeter:", rectangle_perimeter(5, 3))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_perimeter(7))

print("Cuboid Surface Area:", cuboid_tsa(5, 3, 4))
print("Cuboid Volume:", cuboid_volume(5, 3, 4))

print("Sphere Surface Area:", sphere_tsa(7))
print("Sphere Volume:", sphere_volume(7))


