marks = int(input("Enter your marks: "))
if marks < 40:
    print("Failed")
elif marks >= 40 and marks < 60:
    print("Passed")
elif marks >= 60 and marks < 80:
    print("Credit")
elif marks >= 80 and marks <= 100:
    print("Distinction")
else:
    print("Out of range.")
