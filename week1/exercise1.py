"""Your very first python program!

TODO: write a python script that first prints "hello world!"
"""
print("hello world!")

string = “minValue={}maxValue={}”
for i in range(1,6):
	print(string.format(i, i*2))