def calculate_total(exp):
    total=0
    for i in exp :
        total+=i
    return total

tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)
print("Tom's total expense: ",toms_total)
print("Joe's total Expense: ",joes_total)

def sum(a,b):
    total=a+b
    return total
print("Total Expense of both users: ",sum(toms_total,joes_total))
