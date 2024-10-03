d= {'tom': 9130091352, 'rob':8888661008}
print(d['tom'])
d['sam']=7058545663
print(d)

del d['tom']
print(d)
for i in d:
    print("Key",i,"Value",d[i])

print('tom' in d)

d.clear()
print(d)

# tuples
point=(5,9) #here 5 & 9 have different meanings as both can be treated as X and Y co ordinates or something else
