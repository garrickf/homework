import re

"""
Regular expressions exercise
---
0. Create a regex that captures the names of fruit (apple, banana, etc.)
1. Create a regex that captures words that have all vowels (aeiouy) in them in order
2. Create a regex that can scrape phone numbers
3. Create a regex that can scrape email addresses

For each exercise, replace None with your desired regex.
"""

def exercise_0(target):
	"""
	BEGIN YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	regex = None
	"""
	END YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	
	assert(regex != None)
	matches = re.findall(regex, target)
	return process_matches(matches, target)

def exercise_1(target):
	"""
	BEGIN YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	regex = None
	"""
	END YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	
	assert(regex != None)
	matches = re.findall(regex, target)
	return process_matches(matches, target)

def exercise_2(target):
	"""
	BEGIN YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	regex = None
	"""
	END YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	
	assert(regex != None)
	matches = re.findall(regex, target)
	return process_matches(matches, target)

def exercise_3(target):
	"""
	BEGIN YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	regex = None
	"""
	END YOUR CODE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	
	assert(regex != None)
	matches = re.findall(regex, target)
	return process_matches(matches, target)

def process_matches(matches, target):
	print("found: " + str(matches) + " in '" + target + "'")
	return len(matches)

def check(function, input, num_matches):
	l = function(input)
	if l == num_matches:
		print("Got the number of correct matches!")
	else:
		print("Hmm, you got " + str(l) + " matches when you should have gotten " + str(num_matches) + ". Are you missing something?")

def main():
	print("This checks each of the exercises on a chunk of text.")
	print("-----------------------------------------------------\n")
	print("P0:")
	check(exercise_0, "apple banana orange Apple Banana Orange", 6)
	print("\n")

	print("P1:")
	check(exercise_1, "aeiouy, yuoiea", 1)
	check(exercise_1, "abstemiously, adventitiously, facetiously, and sacrilegiously are part of the set", 4)
	print("\n")

	print("P2:")
	check(exercise_2, "(123) 456-7890", 1)
	check(exercise_2, "1234567890, 123-456-7890, (123)4567890, (123)-456-7890, 123.456.7890, +1 (123)456-7890", 6)
	print("\n")

	print("P3:")
	check(exercise_2, "jerry@gmail.com", 1)
	check(exercise_2, "arnold@hotmail.com, garrick97@stanford.edu, garrick@cs.stanford.edu, garrick (at) stanford (dot) edu", 4)
	print("\n")

if __name__ == "__main__":
	main()