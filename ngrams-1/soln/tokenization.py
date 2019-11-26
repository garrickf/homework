"""
N-grams exercise 1
---
Let do a primer on the sliding window technique and get an intution for the
types of predictions n-grams is making and the accuracy of those predictions.
"""

import collections
import random
random.seed(1) # Set random seed so that output can be compared


def preprocess(tokens, ngrams=1):
    """
    To preprocess input, prepend n-1 '<s>' tokens to tokens, and append n-1 '</s>'
    tokens. This is optional, but desired: it lets you start from the very beginning
    of the sentence.
    """
    start = ['<s>'] * (ngrams)
    end = ['</s>'] * (ngrams)
    tokens = start + tokens + end

    return tokens


def vocabulary(tokens):
    return set(tokens)


def process_tokens(tokens, ngrams=1):
    """
    Implements the sliding window technique: keeps a sliding window of size [ngrams],
    and builds a map from the sliding window (as a key) to the list of words that
    could follow it.
    """
    # Initialize map of maps. The internal map's counts start at zero.
    token_map = collections.defaultdict(lambda: collections.defaultdict(int))
    
    window = []
    for token in tokens:
        if len(window) == ngrams:
            token_map[tuple(window)][token] += 1
            window.pop(0)

        window.append(token)
    return token_map


def probability(token_map, vocab, word, history, ngrams=1):
    """
    If given the map and a key, get back the probability of the word occurring 
    given the history. This amounts to counting the number of times the word occurs
    in the map.

    Should never return 0 (use add-1 smoothing).
    """
    assert(len(history) == ngrams)
    history = tuple(history)
    n = len(vocab)

    # BEGIN CODE
    count = 0
    total = 0
    for c in token_map[history].values():
        total += c

    return (token_map[history][word] + 1) / (total + n)


def perplexity(test, token_map, vocab, ngrams=1):
    """
    Compute the perplexity of the lenguage model on a test set. The perplexity is
    the inverse probability of the test set, normalized by the number of words:

    PP(W) = P(w1, w2, ..., wn) ^ (-1 / n)

    Should handle zero probabilities (how could we handle words we haven't seen
    before?)
    """
    tokens = test.split()
    n = len(tokens)
    tokens = preprocess(tokens, ngrams=ngrams)
    
    window = tokens[:ngrams]
    p = 1
    for i in range(ngrams, len(tokens)):
        next_token = tokens[i]

        p *= 1 / probability(token_map, vocab, next_token, window, ngrams=ngrams)

        window.append(next_token)
        window.pop(0)

    PP = p ** (1 / n)
    return PP


SENTENCE = 'the quick brown fox jumped over the lazy dog.'
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] * 50
random.shuffle(NUMBERS)
NUMBERS = ' '.join(NUMBERS)

NUMBERS_TEST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(NUMBERS_TEST)
NUMBERS_TEST = ' '.join(NUMBERS_TEST)

TEXT_TEST = 'One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination.'
def main():
    print('Process tokens tests...')
    
    tokens = SENTENCE.split()
    tokens = preprocess(tokens, ngrams=1)
    # Check preprocessing
    assert(tokens[0] == '<s>')
    assert(tokens[1] == 'the')
    assert(tokens[-1] == '</s>')
    assert(tokens[-2] == 'dog.')

    vocab = vocabulary(tokens)
    assert(len(vocab) == 10)

    token_map = process_tokens(tokens, ngrams=1)
    # Check processing
    assert(len(token_map[tuple(['<s>'])]) == 1)
    assert(len(token_map[tuple(['the'])]) == 2)
    assert(token_map[tuple(['the'])]['quick'] == 1)
    assert(token_map[tuple(['quick'])]['unk'] == 0)

    p = probability(token_map, vocab, 'quick', ['the'], ngrams=1)
    # Check probability
    assert(p == 1/6)

    PP = perplexity('the lazy dog.', token_map, vocab, ngrams=1)
    # Check perplexity
    assert(PP - 9.99 < 10e-3) # Will be artificially low

    # Test on numbers
    print('Testing on numbers...')
    for i in range(1, 3+1):
        tokens = NUMBERS.split()
        tokens = preprocess(tokens, ngrams=i)
        token_map = process_tokens(tokens, ngrams=i)
        PP = perplexity(NUMBERS_TEST, token_map, vocab, ngrams=i)
        print('{}-gram model perplexity: {}'.format(i, PP))
    # QUESTION: what happens here? Why does the perplexity go up?

    print('Testing on text...')
    with open('mlk-i-have-a-dream.txt', 'r') as f:
        text = f.readline()
    for i in range(1, 3+1):
        tokens = text.split()
        tokens = preprocess(tokens, ngrams=i)
        token_map = process_tokens(tokens, ngrams=i)
        PP = perplexity(TEXT_TEST, token_map, vocab, ngrams=i)
        print('{}-gram model perplexity: {}'.format(i, PP))
    # QUESTION: is this better? What changed? Why do you think the peerplexity goes up
    # with the 3-gram model?

if __name__ == '__main__':
    main()
