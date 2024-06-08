#!/usr/bin/env python3

def return_evens(num_list):
    # returns the evens, if there are no even numbers, returns an empty list
    return [num for num in num_list if num % 2 == 0]
    

print(return_evens(range(1,10,2)))


def make_exclamation(sentence_list):
    # returns a list of sentences with exclamation marks at the end of each string.
    return [sentence + "!" for sentence in sentence_list]


print(make_exclamation(["Hello", "Gamze"]))
