import pandas as pd
import numpy as np
import os
import re
import collections

class NaiveBayesModel():
	def __init__(self):
		self.pos_counts = collections.defaultdict(int)
		self.neg_counts = collections.defaultdict(int)
		self.pos_words_seen = 0
		self.neg_words_seen = 0
		self.pos_documents = 0
		self.neg_documents = 0
		self.total_documents = 0
		

	def update(self, tokens, label):
		"""
		Given tokens and label, update:
		1) The prior probability P(c), whether the document is positive or negative
		   based on what we've seen so far
		2) The conditional probability P(o[1:n]|c), the probability of seeing a
		   feature (for us, the occurence of a word) given class c
		"""
		self.total_documents += 1

		if label = 0:
			self.neg_documents += 1
			for token in tokens:
				self.neg_counts[tokens] += 1
				self.neg_words_seen += 1
		else:
			self.pos_documents += 1
			for token in tokens:
				self.pos_counts[tokens] += 1
				self.pos_words_seen += 1


	def predict(self, tokens):
		# TODO: complete

		return label


	def __str__(self):
		return 'I am a naive bayes model!'


def read_lines(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	return lines


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


def tokenize(input):
	"""
	Given a review, return a bag of words representation. We don't care about 
	duplicate words, so they should only appear once. For now, split naively on
	whitespace characters. Strip punctuation [.!?] and make all tokens lowercase

	Example input: "The quick brown fox jumped over the lazy dog."
	Example output: ["the", "quick", "brown", "fox", "jumped", "over", "lazy", "dog"]
	* order does not matter!
	"""
	pattern = '[\.!?]'
	sanitized = re.sub(pattern, '', input.lower())
	return list(set(sanitized.split()))


def train():
	train_dir = 'data/train'
	"""
	Load the examples from the training directory, then update the Naive Bayes 
	model for each example.
	"""
	nb = NaiveBayesModel()
	train_data = load_data(train_dir)
	for example, label in train_data:
		tokens = tokenize(example)
		nb.update(tokens, label)


def test():
	train_dir = 'data/test'
	# TODO: fill this out
	pass


def main():
	print('This exercise does Naive Bayes sentiment classification.')
	print(tokenize('This exercise does Naive Bayes sentiment classification.'))
	load_data('data/train')
	train()


if __name__ == '__main__':
	main()
