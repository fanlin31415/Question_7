# Question 7.1 b)

def C2I(input_file_name, output_file_name, L1, L2):
	f_in = open(input_file_name, 'r')
	f_out = open(output_file_name, 'w')
	f_out.write('index\n')
	for line in f_in:
		coordinate = line.replace('\t', ' ').replace('\n', '').split(' ')
		x1, x2 = coordinate[0], coordinate[1]
		if x1.isdigit():
			x1 = int(x1)
			x2 = int(x2)
			index = x2*L1 + x1
			f_out.write(str(index) + '\n')
	f_out.close()
	f_in.close()

C2I('input_coordinates_7_1.txt','output_index_7_1.txt',50,57)


def I2C(input_file_name, output_file_name, L1, L2):
	f_in = open(input_file_name, 'r')
	f_out = open(output_file_name, 'w')
	f_out.write('x1\tx2\n')
	for line in f_in:
		index = line.replace('\n', '')
		if index.isdigit():
			index = int(index)
			x2 = index // L1
			x1 = index - L1 * x2
			f_out.write(str(x1) + '\t' + str(x2) + '\n')
	f_out.close()
	f_in.close()

I2C('input_index_7_1.txt','output_coordinates_7_1.txt',50,57)