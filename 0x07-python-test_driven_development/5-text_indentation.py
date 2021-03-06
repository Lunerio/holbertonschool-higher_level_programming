#!/usr/bin/python3
"""
a function that prints a text
with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    separators = [".", ":", "?"]
    n_l = list(text)

    for i in range(len(n_l)):
        if n_l[i] in separators:
            if n_l[i + 1] is " ":
                n_l[i + 1] = '\n\n'
            else:
                n_l.insert(i + 1, "\n")
    n_t = ""
    n_t = n_t.join(n_l)
    print("{}".format(n_t), end="")
