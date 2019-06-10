import re

def sum_func(num_list):
	sum =0 
	for i in num_list:
		if i == '':
			num = 0
		else:
			num = int(i)
			if num < 0:
				raise ValueError('Negatives not allowed')
			elif num > 1000:
				num = 0
		sum += num
	return sum

def add(num):
	search1 = re.search('^//(.*)', num)
	if num == '':
		num_list = []
	elif '[' in num:
		cnt = 0
		for i in num:
			if i == '[':
				cnt += 1
		delim = '\[(.*)]' * cnt
		search = re.search(f'^//{delim}+', num)
		if search:
			delimiter = ''
			for i in range(cnt):
				delimiter += search.groups()[i]
			num_list =  re.split('['+delimiter+'\n\]\[]', num[4 + len(delimiter):])
	elif search1:
		delimiter = search1.groups()[0]
		num_list = re.split('['+delimiter+'\n]', num[3 + len(delimiter):])
	else:
		num_list = re.split('[,\n]', num)
	return sum_func(num_list)