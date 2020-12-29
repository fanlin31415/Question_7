
# Question 7.2 b)

def C2I(input_file_name, output_file_name, L):
	L.insert(0,1)
	f_in = open(input_file_name, 'r')
	f_out = open(output_file_name, 'w')
	f_out.write('index\n')
	for line in f_in:
		coordinates = line.replace('\t', ' ').replace('\n', '').split(' ')
		if coordinates[0].isdigit():
			index = 0
			product = 1
			for i in range(len(coordinates)):
				index += int(coordinates[i]) * product
				product *= L[i+1]
			f_out.write(str(index) + '\n')

	f_out.close()
	f_in.close()

C2I('input_coordinates_7_2.txt', 'output_index_7_2.txt', [4,8,5,9,6,7])

def I2C(input_file_name, output_file_name, L):
	f_in = open(input_file_name, 'r')
	f_out = open(output_file_name, 'w')

	head = ''
	for i in range(len(L)):
		head += 'x'+str(i+1)+'\t'
	head += '\n'
	f_out.write(head)

	pre_prod = pre_product(L)

	for line in f_in:
		#process one index
		index = line.replace('\n', '')
		if index.isdigit():
			index = int(index)
			coordinates = [0]*len(L)
			for i in range(len(L)-1, -1, -1):
				remainder = index - dot_product(pre_prod, coordinates)
				x = remainder // pre_prod[i]
				coordinates[i] = x

			row = ''
			for coordinate in coordinates:
				row += str(coordinate) + '\t'
			row += '\n'
			f_out.write(row)


def pre_product(l):
	res = [1] * len(l)
	for i in range(1, len(l)):
		res[i] *= res[i-1] * l[i-1]
	return res

def dot_product(u, v):
	res = 0
	for x, y in zip(u, v):
		res += x * y
	return res

I2C('input_index_7_2.txt', 'output_coordinates_7_2.txt', [4,8,5,9,6,7])