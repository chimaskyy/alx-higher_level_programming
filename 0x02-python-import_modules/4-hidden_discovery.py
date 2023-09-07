#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":

    var = dir(hidden_4)
    for names in var:
        if names[0:2] != "__":
            print(names)
