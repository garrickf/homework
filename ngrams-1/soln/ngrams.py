"""
N-grams exercise 2
---
Let's get an intuition for how n-grams works by generating output
in the style of Alice in Wonderland!
"""

import collections
import random


def process_tokens(filestream, map):
	"""
	Given a filestream object and a dictionary mapping bigrams to the possible
	words that may come after it. The technique is as follows:
	- Keep track of a sliding window of two words. This becomes our key into
	  the map.
	- When we see a new token, store it in the map under the current key; then,
	  update the key for the next iteration.

	Note that this techniques eschews the use of the beginning and end sentence
	tokens (what are the disadvantages of this approach?).
	"""
	window = []
	for token in filestream:
		if len(window) == 2:
			map[tuple(window)].append(token)
			window.pop(0)

		window.append(token)


def generate_text(map, n_words=20):
	"""
	If given the bigram map, generating a string of text isn't too bad. To do it:
	- Pick a key at random from the map to serve as our 'seed.'
	- Follow the seed key to the list of words that could possibly follow it. Pick
	  a word at random from the list, adding it to the output.
	- Update the key with the new word (similar to the sliding window technique)
	  and continue!
	"""
	window = list(random.choice(list(map.keys())))
	processed = ' '.join(window)
	for i in range(n_words):
		to_choose = map[tuple(window)]
		next_word = random.choice(to_choose)
		processed += ' {}'.format(next_word)
		window.append(next_word)
		window.pop(0)
	print('...{}...'.format(processed))


class FileStream:
	"""
	The FileStream encapsulates a file and abstracts the notion of pulling a new
	token aways from the client code. Supports iteration, so the class can be
	used like this:

	for token in filestream_instance:
		# Do something...

	"""
	def __init__(self, filename):
		try:
			self.f = open(filename, 'r')
		except:
			raise Exception('Unable to open file {}.'.format(filename))

		self.cached_line = []

	def get_next(self):
		while True:
			if self.cached_line: # More pythonic than len(self.cached_line)
				next_token, self.cached_line = self.cached_line[0], self.cached_line[1:]
				return next_token
			else:
				line = self.f.readline()
				if not line: # End of file, raise exception
					raise StopIteration()
				else:
					self.cached_line = line.split()

	def __iter__(self):
		return self

	def __next__(self):
		return self.get_next()


def main():
	bigram_map = collections.defaultdict(list) # Create a map from bigrams to possible words

	try:
		filestream = FileStream('alice-in-wonderland.txt')
	except Exception as err:
		print(err)
		exit()

	process_tokens(filestream, bigram_map)
	generate_text(bigram_map)


if __name__ == '__main__':
	main()
