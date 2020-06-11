# put your python code here
a = int(input())
b = int(input())
c = int(input())

list=[a, b, c]

for n, i in enumerate(list):
	mod = i % 2
	if mod > 0:
		list[n] = list[n] + 1

print(int((sum(list)/2)))

