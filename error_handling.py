"""
Error Handling
(1) User Input
(2) Syntax error
(3) Logic error
"""

first_num = input("Enter the first number: ")
sec_num = input("Enter the second number: ")
op = input("Enter the operator(+, - , *, /): ")

try:
    first_num = int(first_num)
    sec_num = int(sec_num)
    output = True
    if op == "+":
        result = first_num + sec_num
    elif op == "-":
        result = first_num - sec_num
    elif op == "*":
        result = first_num * sec_num
    elif op == "/":
        result = first_num / sec_num
    else:
        output = False
        print("Wrong operator!")
    if output:
        print(result)

except: print("Enter number only!")

from create_function import multiply
multiply(4,5)
