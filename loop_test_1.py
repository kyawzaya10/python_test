"""
Loop (for / while)
"""

my_list = [1, 2, 3, 4, 5, 6, "apple"]

for x in my_list:
    print(x)
for y in range(1, 10, 2):
    print(y)
for (a, b) in enumerate(my_list):
    print(a)
    print(b)
print(list(enumerate(my_list)))
