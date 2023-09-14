#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = max(a_dictionary.values())
    for keys in a_dictionary:
        if a_dictionary[keys] == score:
            return keys
