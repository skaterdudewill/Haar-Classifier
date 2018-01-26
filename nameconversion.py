imagePath = 'negatives.txt'
file = open(imagePath, 'r')
for line in file:
	write(line = line[0:line.find('.pgm')])
file.close
