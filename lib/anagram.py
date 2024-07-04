# your code goes here!
#my anagram detector
#You'll need to iterate over the list of words that the match() method takes as an argument. You will compare each word of that list to the word that the Anagram class is initialized with.

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []
        for word in words:
            if sorted(self.word) == sorted(word):
                matches.append(word)
        return matches

