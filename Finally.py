def process_file():
    try:
        f=open('final.txt','w')
        x=1/0
    except FileNotFoundError as e:
        print("Inside except")
    finally:
        print("I am cleaning up file")
        f.close()

process_file()