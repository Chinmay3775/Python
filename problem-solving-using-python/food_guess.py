indian=["samosa","dal","naan","paneer"]
chinese=["noodles","fried rice"]
italian=["pizza","pasta"]

dish=input("Enter the dish ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Not in the list")