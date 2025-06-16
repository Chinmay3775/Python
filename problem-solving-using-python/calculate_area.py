def area_triangle(b,h):
    area=0.5*(b*h)
    return area
def area_rectangle(l,w):
    area=l*w
    return area

base=input("Enter base of triangle ")
base=int(base)
height=input("Enter height of triangle ")
height=int(height)

print("Area of Triangle: ",area_triangle(base,height))

length=input("Enter length of rectangle ")
lenght=int(length)
width=input("Enter width of rectangle ")
width=int(width)

print("Area of Rectangle: ",area_rectangle(lenght,width))