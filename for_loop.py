expenses=[1000,1230,1102,1455,2000]
#total= expenses[0]+expenses[1]+expenses[2]+expenses[3]+expenses[4]
total=0
for i in expenses:
    total= total+i
print(total)

for i in range(len(expenses)):
    print("Month: ",(i+1),"Expense: ",expenses[i])

print("Total: ",total)