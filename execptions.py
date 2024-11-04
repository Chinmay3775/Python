x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division By Zero Exception: ",e)
    z=None
except TypeError as e:
    # print('Exception type: ',type(e).__name__) 
    # This statement is used to identify the type of error 
    # which is occurring in the code but there is a slight change We need to make 
    # that is we have to change the typeerror to 'Exception as e'
    print('Type Error exception....')
    z=None
print("Division is: ",z)