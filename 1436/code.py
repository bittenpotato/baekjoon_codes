order = int(input())
current = 0
num = 666

def isDoomed(num):
		num = str(num)
		for id in range(0, len(num)-2):
			if num[id:id+3] == "666":
				return True
		return False

while True:
	if isDoomed(num):
		current += 1
	if current == order:
		print(num)
		break
	num += 1
