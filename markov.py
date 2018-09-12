"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string, num):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - num):
        string = []

        string = words[i:num + i]
    
        key = tuple(string)
        
# Check to see if key exists in our dictionary
        if key in chains:

#if it exists, append word to the list (value)
            chains[key].append(words[i + num])
            
#if it doesn't exist, create a new list
        else:
            chains[key] = [words[i + num]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    capital_keys = []

    for key in chains.keys():
        if key[0] == key[0].title() and key[0][0].isalpha():
            capital_keys.append(tuple(key))

    first_set = choice(capital_keys)

    key_num = len(first_set)
# Getting random value of chosen key

    next_word = choice(chains[first_set])

# Add first_set and next_word to words
    for i in range(key_num):
        words+= [first_set[i]]

    words += [next_word]

    new_key = first_set[1 :key_num] + tuple([next_word])
    
# making loop for finding the next key wanted
    while new_key in chains:    
        new_next_word = choice(chains[new_key])
        
        words.append(new_next_word)

        new_key = new_key[1 :key_num] + tuple([new_next_word])


    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 3)

random_text = make_text(chains)

print(random_text)
