key_location="chair"
locations=["Garage","Living room","chair","closet"]
for i in locations:
    if i==key_location:
        print("Key found in ", i)
        break
    else:
        print("key not found")