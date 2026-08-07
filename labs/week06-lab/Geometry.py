
def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * base
    print(f"triangle with height {height} and base {base}")
    print(f"Area = 0.5*{height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_circle_area(5, 3)
calculate_circle_area(10, 7)

def calculate_circle_area(radius):
    """Calculates and displays rectangle area"""
    area = 3.1416 * radius * radius
    print(f"circle with radius {radius}")
    print(f"Area = 3.1416*{radius}**2= {area:.2f}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(10)

 def calculate_sphere(radius):
   """Calculates and displays sphere volume"""
   volume = 4.0 / 3 * pi * radius ** 3
   print(f"Sphere with radius {radius}")
   print(f"Volume = 4/3 * π * {radius}³ = {volume:.2f}")
   print()

print("Calculating sphere volumes:")
calculate_sphere(5)
calculate_sphere(10)
