"""
Calculates additional functional dependencies when implementing a database
using Armstrong's Axioms. This script will apply the reflexivity, augmentation,
and transitivity rules to a given set S.

Input: S (list of tuples). A tuple: (X, Y) means X -> Y
Output: S+ (set). This includes the original set S and additional dependencies
"""

def armstrongsAxioms(fd):
    if not isinstance(fd, list):
        raise TypeError("Expected list, got %s", type(fd))
    
    toReturn = fd
    
    # Apply reflexivity rule