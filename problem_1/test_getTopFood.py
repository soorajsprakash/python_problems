from getTopFood import *


def test_getTopFood():
	assert getTopFood('logs/customers.log') == "food1, food4, food5"
	assert getTopFood('logs/one.log') == "Duplicate entry found"
	assert getTopFood('logs/two.log') == "food1, food2, food3"
	assert getTopFood('logs/three.log') == "food1, food5, food2"
	assert getTopFood('logs/four.log') == "File not found"
	assert getTopFood('logs/five.log') == "Empty file"
	assert getTopFood('logs/six.log') == "food5, food1, food2"
