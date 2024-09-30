
str1="hello"
str2="world"
str3=str1+" "+str2
print(len(str1))
print(len(str3))

print(str1[4])
print(str3[2:len(str3)])

print(str3[-10:-1])
print(str3.endswith("rld"))
str3=str3.capitalize();
print(str3)

print(str3.replace("w","W"))

print(str3.find("o"))
print("count",str3.count("o"))

dollar="& is a dollar &&&"
print(dollar.count('$'))


