'''print("Enter your code below \nType #done to finish.")
  
r = open("User_Code.txt", "w")
cmmd  = ""
while cmmd !=  "#done":
    cmmd = input(">>> ")
    r.write(str(cmmd) + "\n")

script = open("User_Code.txt", "r").read()
print(script)
'''
script = "df = pandas.DataFrame(range(10)"

cnt = 0
for letter in script:
    if letter == "\n" or letter == " ":
        pass
    else:
        cnt += 1
print("There are", cnt, "Characters in your script\n")

each_line = script.split("\n")

lp, rp = '(', ')'
lb, rb = '[', ']'


line = 0
No_Errors = 0
for x in script.split("\n"):
    if (lp in x and not rp in x) or (rp in x and not lp in x):
        print("Missing","'" + lp + "'" if not lp in x else rp , 'on line',line)
        print("Line", line, ":", x)
        No_Errors += 1
        
    elif (lb in x and not rb in x) or (rb in x and not lb in x):
        print("Missing","'" + lb + "'" if not lb in x else rb , 'on line',line)
        print("Line", line, ":", x)
        No_Errors += 1
        
    else:
        pass
    print("\n")
    line += 1
    

print("Found", No_Errors,"error" if No_Errors == 1 else "errors" )




