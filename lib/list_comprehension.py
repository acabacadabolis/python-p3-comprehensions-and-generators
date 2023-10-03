#!/usr/bin/env python3

def return_evens(num_list):
    evens = [item for item in num_list if item % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    new_sentence = [string+"!" for string in sentence_list if type(string)==type("asd")]
    return new_sentence
    