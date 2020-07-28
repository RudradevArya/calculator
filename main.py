print("calculator")
print("what is the first number")
firstnum = input()
firstnum = float(firstnum)
print("what is the second number")
secnum = input()
secnum = float(secnum)
print("what will you do with it")
print("Add (+)")
print("subtract(-)")
print("multiply(*)")
print("Divide(/)")
operator = input()
if operator == "Add" or "+":
  print("the total is")
  totaladd = firstnum + secnum
  print(totaladd)
elif operator == "subtract" or "-":
  print("The total is ") 
  totalsub = firstnum - secnum
  print(totalsub)
elif operator == "Multiply" or "*":
  print("the total is ") 
  totalmul = firstnum * secnum
  print(totalmul)
elif operator == "Divide" or "/":
  print("the total is") 
  totaldiv = firstnum / secnum
  print(totaldiv) 

  