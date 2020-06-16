"""
Calculates additional functional dependencies when implementing a database
using Armstrong's Axioms. This script will apply the reflexivity, augmentation,
and transitivity rules to a given set S.

Input: S (list of tuples). A tuple: (X, Y) means X -> Y
Output: S+ (set). This includes the original set S and additional dependencies
"""
import copy
def armstrongsAxioms(fd):
    if not isinstance(fd, list):
        raise TypeError("Expected list, got %s", type(fd))
    
    toReturn = copy.deepcopy(fd)
    
    # Apply reflexivity rule
    for rel in fd:
        if not isinstance(rel, tuple):
            raise TypeError("Expected tuple, got %s", type(rel))
        if (len(rel[0]) > 1):
            # Add additional functional dependencies to toReturn
            listOfSubstrings = []
            for i in range(len(rel[0])):
                for end in range(i+1, len(rel[0])+1):
                    listOfSubstrings.append(rel[0][i: end])
            listOfSubstrings.remove(rel[0])
            # Add each substring to toReturn
            for substr in listOfSubstrings:
                toReturn.append((rel[0], substr))
    print(toReturn)
armstrongsAxioms([("abc", "d")])
                