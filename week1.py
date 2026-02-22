# Warmups
def twosum(arr, target):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
              return [i, j]
    return [-1, -1]


def foobarbaz(n):
    result = []
    counter = 0

    for i in range(1, n+1):
        if i % 3 == 0:
            counter += 1
            if counter % 3 == 1:
                result.append('foo')
            elif counter % 3 == 2:
                result.append('bar')
            else:
                result.append('baz')
        else:
            result.append(str(i))

    return result

import string

def sentence_palindrome(sentence):
    """
    Return true if the sentence is a palindrome. Ignore case, spaces, and punctuation.
    Hint: you can import the `string` module and `string.punctuation` to get a list of punctuation characters to ignore.
    """
    cleaned = ""
    for char in sentence:
        if char not in string.punctuation and char != ' ':
            cleaned += char.lower()
    
    # Check if it's the same forwards and backwards
    return cleaned == cleaned[::-1]


def dyslexic_palindrome(word):
    """
    Return true if the input word is a palindrome. However, the letters d, p, b, and q are considered interchangeable.
    """
    dyslexic_letters = {'d', 'p', 'b', 'q'}
    reversed_word = word[::-1]
    
    for i in range(len(word)):
        left = word[i]
        right = reversed_word[i]
        
        if left == right:
            continue
        elif left in dyslexic_letters and right in dyslexic_letters:
            continue
        else:
            return False
    
    return True


def local_minimums(arr):
    """
    Given an array of integers, return a list of indexes the local minimums.
    A local minimum is a number which is less than its neighbors.
    """
    result = []

    for i in range(len(arr)):
        if i == 0: # first number
            if len(arr) > 1 and arr[i] < arr[i+1]:
                result.append(i)
        elif i == len(arr) - 1: #last number
            if arr[i] < arr[i-1]:
                result.append(i)        
        else:
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                result.append(i)
    
    return result

# Now that you're warmed up

def count_clumps(arr):
    """
    Return the number of clumps in the input list.
    A clump is a series of 2 or more adjacent elements of the same value.
    """
    number_of_clumps = 0

    for i in range(len(arr)-1):
        if i == 0:
            if arr[i] == arr[i+1]:
                number_of_clumps += 1
        else:
            if arr[i] == arr[i+1] and arr[i] != arr[i-1]:
                number_of_clumps += 1

    return number_of_clumps


def zero_matrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
    The matrix is passed as a list of lists, e.g:
    [   [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    DO NOT modify the original matrix, instead return a new matrix.
    Be careful when creating the new matrix - there are subtleties about copying lists in Python.
    I would suggest making a blank matrix of the same size as the input matrix, then modifying it.
    Or create the new matrix as you go along.
    Hint: Algorithm should be O(rows*columns) - try to avoid brute forcing.
    Hint: An empty matrix will be passed in as [[]]
    """
    if matrix == [[]] or len(matrix) == 0:
        return [[]]
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_rows = []
    zero_cols = []
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.append(i) 
                zero_cols.append(j)
    
    new_matrix = []
    
    for i in range(rows):
        new_row = []
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                new_row.append(0)
            else:
                new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    
    return new_matrix


def is_anagram(s1, s2):
    """
    Return True if the two input strings are anagrams of each other, False otherwise.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once. Ignore punctuation and capitalization.

    Reminder: Strings are just a collection of characters. Maybe thinking about them like a list will help.
    """
    cleaned_s1 = ""
    for char in s1:
        if char not in string.punctuation and char != ' ':
            cleaned_s1 += char.lower()
    
    cleaned_s2 = ""
    for char in s2:
        if char not in string.punctuation and char != ' ':
            cleaned_s2 += char.lower()
    
    return sorted(cleaned_s1) == sorted(cleaned_s2)