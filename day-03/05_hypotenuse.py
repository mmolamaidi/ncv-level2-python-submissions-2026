# A learner types the two shorter sides of a right-angled triangle in metres. Show the length of the hypotenuse to two decimals.
import math

side1=float(input("Enter the length of a side of a triangle (in meter):" ))
side2=float(input("Enter the length of the other side of a triangle(in meter):"))

# A side that is zero or negative must be rejected with a message.
if side1 >=0 or side2>=0:
    x=(math.pow(side1,2)+math.pow(side2,2))
    hypotenuse= math.sqrt(x)
    print("hypotenuse:", hypotenuse,"m\u00b2")
    print("Accepted")
else:
    print("Rejected")
