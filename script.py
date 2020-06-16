"""
Calculates additional functional dependencies when implementing a database
using Armstrong's Axioms. This script will apply the reflexivity, augmentation,
and transitivity rules to a given set S.

Input: S (list of tuples). A tuple: (X, Y) means X -> Y
Output: S+ (set). This includes the original set S and additional dependencies
"""
import copy
import itertools
def armstrongsAxioms(fd):
    if not isinstance(fd, list):
        raise TypeError("Expected list, got %s", type(fd))
    
    toReturn1 = copy.deepcopy(fd)
    
    # Apply reflexivity rule
    for rel in fd:
        if not isinstance(rel, tuple):
            raise TypeError("Expected tuple, got %s", type(rel))
        if (len(rel[0]) > 1):
            # Add additional functional dependencies to toReturn1
            listOfSubstrings = []
            for i in range(len(rel[0])):
                for end in range(i+1, len(rel[0])+1):
                    listOfSubstrings.append(rel[0][i: end])
            listOfSubstrings.remove(rel[0])
            # Add each substring to toReturn
            for substr in listOfSubstrings:
                toReturn1.append((rel[0], substr))
    print(toReturn1)
    
    # Apply augmentation rule
    # 1. Find all unique characters
    setOfChars = set()
    for rel in fd:
        for attributes in rel[0]:
            for char in attributes:
                setOfChars.add(char)
    print(setOfChars)
    # 2. Get all substrings
    listOfSubstrings = []
    for i in range(1, len(setOfChars)+1):
        for subset in itertools.combinations(setOfChars, i):
            chars = ''
            for char in subset:
                chars = chars + char
            listOfSubstrings.append(chars)
    print(listOfSubstrings)
    # 3. Append substrings of allChars to both sides of relation
    toReturn2 = copy.deepcopy(toReturn1)
    for rel in toReturn1:
        for substr in listOfSubstrings:
            newRel0 = rel[0]
            newRel1 = rel[1]
            for char in substr:
                if (char not in newRel0):
                    newRel0 = newRel0 + char
                if (char not in newRel1):
                    newRel1 = newRel1 + char
            toReturn2.append((newRel0, newRel1))
    print(toReturn2)
armstrongsAxioms([("a", "b"), ("b", "c"), ("cd", "e")])
                