"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        bi_string = (words[i], words[i+1])

# Check to see if key exists in our dictionary
        if bi_string in chains:

#if it exists, append word to the list (value)
            chains[bi_string].append(words[i + 2])

#if it doesn't exist, create a new list
        else:
            chains[bi_string] = [words[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    keys = list(chains.keys())

    first_set = choice(keys)

# Getting random value of chosen key

    next_word = choice(chains[first_set])

# Add first_set and next_word to words
    words.extend([first_set[0], first_set[1], next_word])
    new_key = (first_set[1], next_word)

# making loop for finding the next key wanted
    while new_key in chains:    
        new_next_word = choice(chains[new_key])
        
        words.append(new_next_word)

        new_key = (new_key[1], new_next_word)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
