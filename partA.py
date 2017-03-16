from collections import Counter
import re

## Problem 1 ##
## O(nlogn) polynomial

def tokenize(textFilePath): ## O(n) linear
    try:
        text = open(textFilePath, 'r').readlines()
    except IOError:
        print "File path error."
        return
    lines = []
    for line in text:
        lines.extend(re.sub(r'[^a-zA-Z0-9 ]', ' ', line).lower().split(" "))
    return [line for line in lines if line != '']

def computeWordFrequencies(tokens): ## O(n) linear
    return Counter(tokens)

def printCount(count): ## O(nlogn) polynomial
    for item in sorted(count.items(), reverse=True, key=lambda item: item[1]):
        print item[0] + " " + str(item[1])


if __name__ == "__main__":
    textFilePath = raw_input("Enter file pathname to tokenize and word count: ")

    tokens = tokenize(textFilePath)
    count = computeWordFrequencies(tokens)
    printCount(count)