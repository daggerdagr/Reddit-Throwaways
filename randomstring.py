import string, random

def randomstring(num_chars, special_chars):
	assert num_chars > 0, "We can only give you strings with more than 0 elements"
	if num_chars == 1:
		return string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)]
	return string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] + randomstring(num_chars - 1, special_chars)