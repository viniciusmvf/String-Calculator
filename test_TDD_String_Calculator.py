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

