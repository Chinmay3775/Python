items= ["bread","pasta","Fruits","Veggies"]
print(items)
print(items[0])
items[0]="chips"
print(items)
print(items[0:2])
print(items[-1])
items.append("Butter")
print(items)
items.insert(1,"butter")
print(items)

bathroom=["shampoo","soap"]
all_items=items+bathroom
print(all_items)
print(len(all_items))

print("butter" in all_items)