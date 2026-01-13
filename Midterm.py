import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):

    area = math.pi * (radius ** 2)

    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    if n >= 4:
        for i in range (n):
            for j in range (i + 1):
                if i == 0 or i == n - 1 or j == 0 or j == 2*i + 1:
                    result +="*"
            else:
                result += " "
            if i != n - 1:
                result += "\n"
    else :
        return (f"The triangle height should be at least 4.")

    return result

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""

    if n >= 3:
        for i in range (n):
            for j in range (i):
                result += " "
            for k in range (2*(n - i) - 1):
                result += "*"
            if i != n - 1:
                result += "\n"
    else:
        return (f"The pyramid height should be at least 3.")
    
    return result
# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
