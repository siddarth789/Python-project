x=int(input("Enter a first Number"))
y=int(input("Enter a second Number"))
op=input("Enter a operation(+,-,*,/):")
if op == '+':
    print("Result:",x+y)
elif op == '-':
    print("Result:",x-y)
elif op == '*':
    print("Result:",x*y)
elif op == '/':
    print("Result:",x/y)
else:
    print("not valid please give a valid operation")

# Output :
# Enter a first Number2
# Enter a second Number3
# Enter a operation(+,-,*,/):+
# Result: 5

# Enter a first Number2
# Enter a second Number3
# Enter a operation(+,-,*,/):-
# Result: -1

# Enter a first Number2
# Enter a second Number3
# Enter a operation(+,-,*,/):*
# Result: 6

# Enter a first Number2
# Enter a second Number3
# Enter a operation(+,-,*,/):/
# Result: 0.6666666666666666 '''