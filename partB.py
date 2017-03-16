## Problem 2 ##
## O(n^2) polynomial

from partA import computeWordFrequencies, tokenize

def intersection(textFilePath1, textFilePath2): ## O(n^2) polynomial
    count1 = computeWordFrequencies(tokenize(textFilePath1))
    count2 = computeWordFrequencies(tokenize(textFilePath2))

    count = 0

    for word in count1.keys():
        if word in count2.keys():
            count = count + 1

    print count
    return count


if __name__ == "__main__":
    textFilePath1 = raw_input("Enter file pathname #1 to find intersecting words: ")
    textFilePath2 = raw_input("Enter file pathname #2: ")

    intersection(textFilePath1, textFilePath2)