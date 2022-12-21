Length_1 = float(input("Enter length of the first side of a triangle ="))
Length_2 = float(input("Enter length of the second side of a triangle ="))
Length_3 = float(input("Enter length of the third side of a triangle ="))
if(Length_1<(Length_2 + Length_3) and Length_2<(Length_1 + Length_3) and Length_3<(Length_2 + Length_1)): #We use the given formula to check if the triangle can exist
    print("Yes , It is possible to have a triangle with the  given side lengths")
else:
    print("No , It is not possible to have a triangle with the given sides lengths")
