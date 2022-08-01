

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines



def world_count(lines):
	Allen_word_count = 0
	Allen_stiker_count = 0
	Allen_picture_count = 0
	Viki_word_count = 0
	Viki_stiker_count = 0
	Viki_picture_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				if s[2] == "貼圖":
					Allen_stiker_count += 1
				elif s[2] == "圖片":
					Allen_picture_count += 1
				else:
					Allen_word_count += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				if m == "貼圖":
					Viki_stiker_count += 1
				elif m == "圖片":
					Viki_picture_count += 1
				else:
					Viki_word_count += len(m)
	print("Allen speoken ", Allen_word_count)	
	print("Allen stiker ", Allen_stiker_count)	
	print("Allen picture ", Allen_picture_count)	
	print("Viki speoken ", Viki_word_count)	
	print("Viki stiker ", Viki_stiker_count)	
	print("Viki picture ", Viki_picture_count)
	


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	#print(lines)
	lines = world_count(lines)
	#write_file('output.txt', lines)


main()