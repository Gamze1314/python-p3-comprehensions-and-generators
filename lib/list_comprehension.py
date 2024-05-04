#!/usr/bin/env python3

def return_evens(num_list):
    # returns a list of even elements [0,8]
    # list comprehension
    return [num for num in num_list if (num % 2 == 0)]


return_evens = return_evens([0, 3, 4, 5, 6,])
print(return_evens)


def make_exclamation(sentence_list):
    # returns a list of sentences with exclamation marks at the end of each string.
    return [sentence + "!" for sentence in sentence_list]


sentences = ["This is a sentence.",
             "This is another sentence.", "And this is the last one."]
print(make_exclamation(sentences))
