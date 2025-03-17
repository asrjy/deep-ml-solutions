def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b):
		return -1
	c = []
	row = []
	temp = 0
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				temp += a[i][k] * b[k][j]
			row.append(temp)
			temp = 0
		c.append(row)
		row = []
	return c