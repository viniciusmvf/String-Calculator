from TDD_String_Calculator import add
import pytest

def test_add_empty_string():
	result = add('')
	assert result == 0

def test_add_single_number():
	result = add('4')
	assert result == 4

def test_add_two_numbers():
	result = add('1,2')
	assert result == 3

def test_add_unknown_numbers():
	result = add('1,2,3,4,5,6,7')
	assert result == 28

def test_add_new_lines():
	result = add('1\n2,3')
	assert result == 6
	result = add('1\n2\n3\n4\n5')
	assert result == 15

def test_add_delimiter():
	result = add('//;\n1;2')
	assert result == 3

def test_add_negative_exception():
	with pytest.raises(ValueError):
		result = add('-4')
	with pytest.raises(ValueError):
		result = add('1,-2')
	with pytest.raises(ValueError):
		result = add('1,2,-3,4,5,-6,7')
	with pytest.raises(ValueError):
		result = add('-1\n2,3')
	with pytest.raises(ValueError):
		result = add('1\n2\n3\n-4\n5')
	with pytest.raises(ValueError):
		result = add('//;\n-1;2')

def test_add_greater_than_100():
	result = add('2,1001')
	assert result == 2
	result = add('2,1451,5')
	assert result == 7
	result = add('2\n1001,4521,6,12')
	assert result == 20

def test_add_any_length_delimiter():
	result = add('//[***]\n1***2***3')
	assert result == 6
	result = add('//[***]\n14***21***37')
	assert result == 72
	result = add('//[***]\n5***2***3')
	assert result == 10
	result = add('//[***]\n45***23***1002')
	assert result == 68

def test_add_multiple_delimiters():
	result = add('//[*][%]\n1*2%3')
	assert result == 6
	result = add('//[*][%][=]\n1*2%3=4')
	assert result == 10
	result = add('//[*][%][=][&]\n1*2%3=4&5')
	assert result == 15
	result = add('//[*][%][=][&][$]\n1*2%3=4&5$6')
	assert result == 21

def test_add_any_char_length_delimiter():
	result = add('//[***][%]\n1***2%3')
	assert result == 6
	result = add('//[*][%^%^%^][==]\n1*2%^%^%^3==4')
	assert result == 10
	result = add('//[*][%][=][&****^]\n1*2%3=4&****^5')
	assert result == 15
	result = add('//[*][%%][===][&&&&][$$$$$]\n1*2%%3===4&&&&5$$$$$6')
	assert result == 21