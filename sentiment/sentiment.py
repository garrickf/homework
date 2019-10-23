import os
import re
import collections
from naive_bayes import NaiveBayesModel

"""
sentiment.py

This program does Naive Bayes sentiment classification on movie reviews. Without
any extra features, it can hit up to 80.35% accuracy! Nice!
"""
nb = NaiveBayesModel()

def read_lines(filename):
	"""
	Helper function that just reads all the lines from a file. Assumes the file
	is a single line, so we return lines[0].
	"""
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	return lines[0]


def load_data(directory):
	"""
	Given directory, load all the positive and negative examples into a single
	list with elements of the form (example, label), where label = 1 means positive
	and label = 0 means negative.
	"""
	print('Loading data...')
	pos_path = '{}/pos'.format(directory)
	pos_examples = [(read_lines('{}/{}'.format(pos_path, file)), 1) for file in os.listdir(pos_path)]

	neg_path = '{}/neg'.format(directory)
	neg_examples = [(read_lines('{}/{}'.format(neg_path, file)), 0) for file in os.listdir(neg_path)]
	
	all_examples = pos_examples + neg_examples
	print('Loading data: all done!')
	return all_examples


def tokenize(s):
	"""
	Given a review, return a bag of words representation. We don't care about 
	duplicate words, so they should only appear once. For now, split naively on
	whitespace characters. Strip punctuation [.!?] and make all tokens lowercase

	Example input: "The quick brown fox jumped over the lazy dog."
	Example output: ["the", "quick", "brown", "fox", "jumped", "over", "lazy", "dog"]
	* order does not matter!
	"""
	pattern = '[\.!?]'
	sanitized = re.sub(pattern, '', s.lower())
	return list(set(sanitized.split()))


def train():
	train_dir = 'data/train'
	"""
	Load the examples from the training directory, then update the Naive Bayes 
	model for each example.
	"""
	train_data = load_data(train_dir)

	for example, label in train_data:
		tokens = tokenize(example)
		nb.update(tokens, label)

	nb.compute_probabilities()


def test():
	test_dir = 'data/test'
	"""
	Load the examples from the testing directory, then use the Naive Bayes model 
	to predict the class of the test example. Compare it against the actual label,
	and accumulate a correct counter.
	"""
	test_data = load_data(test_dir)
	
	correct, total = 0, 0
	for example, label in test_data:
		tokens = tokenize(example)
		predicted, score = nb.predict(tokens)
		# print(predicted, score, example)
		if predicted == label:
			correct += 1
		total += 1
	
	print('Accuracy:', correct / total)


def main():
	print('This exercise does Naive Bayes sentiment classification.')
	print('Training...')
	train()
	print('Testing...')
	test()


if __name__ == '__main__':
	main()
