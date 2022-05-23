currentLoc = 1
emptyLoc = 2
wantLoc = 3

def move(currentStack, currentLoc, wantLoc, emptyLoc):
	if currentStack == 1:
		print(currentLoc, wantLoc)
	else:
		move(currentStack-1, currentLoc, emptyLoc, wantLoc)
		print(currentLoc, wantLoc)
		move(currentStack-1, emptyLoc, wantLoc, currentLoc)

currentStack = int(input())
print((2 ** currentStack)-1)
move(currentStack, currentLoc, wantLoc, emptyLoc)
