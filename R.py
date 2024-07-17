import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side * side

def triangle_area(base, height):
    return 0.5 * base * height

def parallelogram_area(base, height):
    return base * height

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def kite_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def pentagon_area(side):
    return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side * side) / 4

def hexagon_area(side):
    return ((3 * math.sqrt(3)) / 2) * side * side

def octagon_area(side):
    return 2 * (1 + math.sqrt(2)) * side * side

def sector_area(radius, angle):
    return 0.5 * radius * radius * math.radians(angle)

def annulus_area(outer_radius, inner_radius):
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)

def segment_area(radius, angle):
    return 0.5 * radius ** 2 * (math.radians(angle) - math.sin(math.radians(angle)))

def display_menu():
    print("Choose a geometrical figure to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Parallelogram")
    print("6. Trapezoid")
    print("7. Ellipse")
    print("8. Rhombus")
    print("9. Kite")
    print("10. Pentagon")
    print("11. Hexagon")
    print("12. Octagon")
    print("13. Sector")
    print("14. Annulus")
    print("15. Segment")
    print("16. Exit")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-16): "))

        if choice == 1:
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is: {circle_area(radius)}")

        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"The area of the rectangle is: {rectangle_area(length, width)}")

        elif choice == 3:
            side = float(input("Enter the side length of the square: "))
            print(f"The area of the square is: {square_area(side)}")

        elif choice == 4:
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print(f"The area of the triangle is: {triangle_area(base, height)}")

        elif choice == 5:
            base = float(input("Enter the base length of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            print(f"The area of the parallelogram is: {parallelogram_area(base, height)}")

        elif choice == 6:
            base1 = float(input("Enter the first base length of the trapezoid: "))
            base2 = float(input("Enter the second base length of the trapezoid: "))
            height = float(input("Enter the height of the trapezoid: "))
            print(f"The area of the trapezoid is: {trapezoid_area(base1, base2, height)}")

        elif choice == 7:
            semi_major_axis = float(input("Enter the semi-major axis of the ellipse: "))
            semi_minor_axis = float(input("Enter the semi-minor axis of the ellipse: "))
            print(f"The area of the ellipse is: {ellipse_area(semi_major_axis, semi_minor_axis)}")

        elif choice == 8:
            diagonal1 = float(input("Enter the first diagonal of the rhombus: "))
            diagonal2 = float(input("Enter the second diagonal of the rhombus: "))
            print(f"The area of the rhombus is: {rhombus_area(diagonal1, diagonal2)}")

        elif choice == 9:
            diagonal1 = float(input("Enter the first diagonal of the kite: "))
            diagonal2 = float(input("Enter the second diagonal of the kite: "))
            print(f"The area of the kite is: {kite_area(diagonal1, diagonal2)}")

        elif choice == 10:
            side = float(input("Enter the side length of the pentagon: "))
            print(f"The area of the pentagon is: {pentagon_area(side)}")

        elif choice == 11:
            side = float(input("Enter the side length of the hexagon: "))
            print(f"The area of the hexagon is: {hexagon_area(side)}")

        elif choice == 12:
            side = float(input("Enter the side length of the octagon: "))
            print(f"The area of the octagon is: {octagon_area(side)}")

        elif choice == 13:
            radius = float(input("Enter the radius of the sector: "))
            angle = float(input("Enter the central angle of the sector (in degrees): "))
            print(f"The area of the sector is: {sector_area(radius, angle)}")

        elif choice == 14:
            outer_radius = float(input("Enter the outer radius of the annulus: "))
            inner_radius = float(input("Enter the inner radius of the annulus: "))
            print(f"The area of the annulus is: {annulus_area(outer_radius, inner_radius)}")

        elif choice == 15:
            radius = float(input("Enter the radius of the segment: "))
            angle = float(input("Enter the central angle of the segment (in degrees): "))
            print(f"The area of the segment is: {segment_area(radius, angle)}")

        elif choice == 16:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
