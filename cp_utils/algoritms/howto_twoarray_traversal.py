
row = 3
col = 4

# 1 2 3 4
# 8 7 6 5
# 9 10 11 12
def forward_backward(row: int, col: int):
	matrix = [[0]*col for _ in range(row)]
	index = 0
	for i in range(row):
		if i%2 == 0:
			start, end, direction = 0, col, 1
		else:
			start, end, direction = col-1, -1, -1
		for j in range(start, end, direction):
			index += 1
			matrix[i][j] = index
	return matrix

# 1 2 3 4
# 10 11 12 5
# 9 8 7 6

def spiral_out_in(row: int, col: int):
	matrix = [[0]*col for _ in range(row)]
	matrix[0] = [i+1 for i in range(col)]
	index = col
	index_col = 1
	index_row = 0
	for i in range(row-index_col):
		index += 1
		matrix[i][index_row] = index
	index_row += 1
	for i in range(col-index_row,):
		index += 1
		matrix[][] = index

	return matrix


def print_matrix(matrix):
	for row in matrix:
		print('\t'.join(map(str,row)))

# print_matrix(forward_backward(row, col))
print_matrix(spiral_out_in(row, col))

