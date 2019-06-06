import re
# import pytest

def sum_func(num_list):
	sum =0 
	for i in num_list:
		if int(i) < 0:
			raise ValueError('Negatives not allowed')
		sum += int(i)
	return sum

def add(num):
	search = re.search('^//(.*)', num)
	if num == '':
		num_list = []
	elif search:
		delimiter = search.groups()[0]
		num_list =  num[3 + len(delimiter):].split(delimiter)
	else:
		num_list = re.split('[,\n]', num)
	return sum_func(num_list)