# write your code here

LEFT, RIGHT, LINE = '| ', ' |', '-' * 9

a = [list(" " * 3) for i in range(3)]


def show():
	print(LINE)
	for op in a: print(LEFT + " ".join(op) + RIGHT)
	print(LINE)


def check(c):
	flag = False
	for i in range(3):
		if a[i][0] == a[i][1] == a[i][2] == c: flag = True
		if a[0][i] == a[1][i] == a[2][i] == c: flag = True

	st1, st2 = set(), set()
	for i in range(3): st1.add(a[i][i]), st2.add(a[i][2 - i])

	return flag or len(st1) == 1 and c in st1 or len(st2) == 1 and c in st2


def fact(c):
	while True:
		try: x, y = input("Enter the coordinates: ").split()
		except:
			print("Please enter two numbers!!!")
			continue

		if not x.isdigit() or not y.isdigit():
			print("You should enter numbers!")
			continue

		x, y = int(x), int(y)
		if x < 1 or y < 1 or x > 3 or y > 3:
			print("Coordinates should be from 1 to 3!")
			continue

		x -= 1;
		y -= 1
		if a[x][y] == 'O' or a[x][y] == 'X':
			print("This cell is occupied! Choose another one!")
		else: a[x][y] = c; break


show()
for i in range(9):
	char = 'X' if not i & 1 else 'O'
	fact(char), show()

	if check(char):
		print(char + " wins")
		break

else: print("Draw")
