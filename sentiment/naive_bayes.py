import numpy as np
import os
import re
import collections

"""
sentiment.py

This program does Naive Bayes sentiment classification on movie reviews. Without
any extra features, it can hit up to 80.35% accuracy! Nice!
"""

class NaiveBayesModel():
	def __init__(self):
		"""
		Constuctor which initializes internal counts and probabilities. You won't
		need to edit this.
		"""
		self.counts = [collections.defaultdict(int), collections.defaultdict(int)]
		self.total_counts = [0, 0]
		self.documents = np.array([0, 0])
		self.total_documents = 0
		
		self.log_prior = np.array([0, 0])
		self.log_likelihood = [collections.defaultdict(int), collections.defaultdict(int)]


	def update(self, tokens, label):
		"""
		Given tokens and label, update:
		1) The prior probability P(c), whether the document is positive or negative
		   based on what we've seen so far
		2) The conditional probability P(o[1:n]|c), the probability of seeing a
		   feature (for us, the occurence of a word) given class c

		In this step, simply accumulate the counts of the information you need. 
		Calculating the log probabilities happens in compute_probabilities.
		Think about adding Laplace smoothing here.
		"""
		"""
		Begin your code
		"""
		
		# TODO: accumulate counts

		"""
		End your code
		"""



	def compute_probabilities(self):
		"""
		Assuming counts are updated, compute the log probabilities and cache them
		for future predictions.
		"""
		# TODO: update the log_prior given label and counts. HINT: np.log can
		# compute the element-wise log for an array. Change the line below.
		self.log_prior = np.array([0, 0])
		for label, counts in enumerate(self.counts):
			# TODO: update the log_likelihood given label and counts. Change the line below.
			self.log_likelihood[label] = collections.defaultdict(int)


	def predict(self, tokens):
		"""
		Given a list of tokens, compute the log probability for each class, then 
		output the maximum class and score associated with that class.
		"""
		log_prob = [0, 0]
		for label in range(len(log_prob)):
			"""
			Begin your code
			"""

			# TODO: accumulate the score log_prob[label] (prior plus all liklihoods)
			
			"""
			End your code
			"""
		return max(zip(range(len(log_prob)), log_prob), key=lambda t: t[1])


	def __str__(self):
		"""
		Debug method which prints out the counts so far. Feel free to edit to your
		convenience.
		"""
		return 'documents: ' + str(self.documents) + '\ntotal: ' + str(self.total_documents) \
			+ '\ncounts: ' + str(self.counts) + '\ntotal: ' + str(self.total_counts)


def main():
	print('Testing the NaiveBayesModel...')
	nb = NaiveBayesModel()
	print('Test: should increment counts properly.')
	train_data = [(["the", "quick", "brown", "fox", "jumped", "over", "lazy", "dog"], 1), (['the'], 0)]
	for tokens, label in train_data:
		nb.update(tokens, label)
	assert(np.array_equal(nb.documents, [1, 1]))
	assert(nb.total_documents == 2)
	assert(nb.counts[1]['the'] == 1)
	assert(nb.counts[0]['quick'] == 1)
	assert('unk' not in nb.counts[0])
	assert(nb.total_counts[1] == 8)

	print('Test: should not compute probabilities after update.')
	assert(np.array_equal(nb.log_prior, [0, 0]))

	print('Test: should compute probabilities when compute_probabilities called.')
	nb.compute_probabilities()
	assert(np.array_equal(nb.log_prior, np.log([0.5, 0.5])))

	print('Test: should predict new document properly.')
	label, score = nb.predict(["the"])
	assert(label == 0)
	label, score = nb.predict(["quick"])
	assert(label == 0)

	# Add a lot of positive examples to tip the scale
	train_data = [(['the'], 1)] * 10
	for tokens, label in train_data:
		nb.update(tokens, label)
	nb.compute_probabilities()
	label, score = nb.predict(["the"])
	assert(label == 1)

	print('All seems good! Carry on.')


if __name__ == '__main__':
	main()
