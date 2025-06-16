book={}
book['tom']={
    'name':'tom',
    'address':'1 blue street,NY',
    'phone':9130091352

}
book['bob']={
    'name':'bob',
    'address':'1 blue street,NY',
    'phone':8888661008
    
}

import json
s=json.dumps(book,indent=4)
#print(s)
with open("D://python//python_programs//book.txt", "w") as f:
        f.write(s)