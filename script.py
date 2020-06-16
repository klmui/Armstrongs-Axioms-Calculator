"""
Calculates additional functional dependencies when implementing a database
using Armstrong's Axioms. This script will apply the reflexivity, augmentation,
and transitivity rules to a given set S.

Input: S (list of tuples). A tuple: (X, Y) means X -> Y. Please represent your 
       attributes in the list of tuples as one character. E.g. id is X. You
       may also combine attributes and represent them as two letters combined.
Output: S+ (set). This includes the original set S and additional dependencies
"""
import copy
import itertools
from collections import defaultdict
def armstrongsAxioms(fds):
    if not isinstance(fds, list):
        raise TypeError("Expected list, got %s", type(fds))
    
    toReturn1 = copy.deepcopy(fds)
    
    # Apply reflexivity rule
    for rel in fds:
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
    #print("toRet1",toReturn1)
    
    # Apply augmentation rule
    # 1. Find all unique characters
    setOfChars = set()
    for rel in fds:
        for attributes in rel[0]:
            for char in attributes:
                setOfChars.add(char)
    #print("setOfChars",setOfChars)
    # 2. Get all substrings
    listOfSubstrings = []
    for i in range(1, len(setOfChars)+1):
        for subset in itertools.combinations(setOfChars, i):
            chars = ''
            for char in subset:
                chars = chars + char
            listOfSubstrings.append(chars)
    #print("listOfSubstrings",listOfSubstrings)
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
            toReturn2.append((''.join(sorted(newRel0)), ''.join(sorted(newRel1))))
    #print("toRet2",list(dict.fromkeys(toReturn2)))
    
    # Apply transitivity rule
    toReturn3 = copy.deepcopy(toReturn2)
    destinations = defaultdict(set)
    for rel in toReturn2:
        destinations[rel[0]].add(rel[1])
    #print("dests",destinations)
    for key, value in destinations.items():
        for dest in value:
            if (dest in destinations.keys()):
                for char in destinations[dest]:
                    newTuple = (key, char)
                    toReturn3.append(newTuple)
    #print("toRet3", toReturn3)
    
    # Print out all functional dependencies
    for fd in toReturn3:
        print(fd)
        
"""
ENTER YOUR INPUT BELOW. The first value in the tuple represents the attribute(s) that
determines the attribute(s) in the second value of the tuple. 

Make sure to represent your attributes as a single character as shown below. 
For example, id is x.
Just modify the example below.
"""
armstrongsAxioms([("a", "b"), ("b", "c"), ("cd", "e")])
                
