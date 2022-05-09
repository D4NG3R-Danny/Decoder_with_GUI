#Author:D4NG3R-D4NNY
def letter_count(text: str)-> dict:
    counter = {}
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for alphas in alphabet:
        counter.setdefault(alphas,-1)
        counter[alphas] += 1
    for letters in text:
        counter.setdefault(letters,0)
        counter[letters] += 1
    return counter