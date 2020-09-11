import random
from collections import defaultdict

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()

m_dict = defaultdict(list)
# TODO: analyze which words can follow other words
# Your code here
for word, next_word in zip(word_list[0:-1], word_list[1:]):
    m_dict[word].append(next_word)

m_dict = dict(m_dict)


# TODO: construct 5 random sentences
# Your code here
word1 = random.choice(list(m_dict.keys()))
sentence = word1.capitalize()
for i in range(5):
    sentence = ""
    for i in range(15):
        word2 = random.choice(m_dict[word1])
        word1 = word2
        sentence += " " + word2
    sentence += "."
    print(sentence)
