# Mirror Pairs Finder

A competitive programming solution that finds the largest palindromic number 
that can be created by concatenating two numbers from an input dataset.

## Problem
Given a list of numbers, find the maximum palindrome that can be formed by 
concatenating any two different numbers from the list.

**Example:**
- Input: `24 79 42 97 123 124`
- Output: `42124` 

## Optimization Techniques

1. Two-Character Hash Table Grouping**: Groups numbers by their first two 
   digits, heavily reducting the amount of canidate pairs.
   
2. **Early Exit Checks**: Validates character matches before full palindrome 
   verification
   
3. **Efficient Palindrome Detection**: Two-pointer algorithm that exits 
   immediately on mismatch

## Performance
- Handles 100,000 numbers in ~0.4 seconds
- 100x speedup due to the two-character hash table grouping.
- Optimized for Irish Informatics Olympiad constraints

## Constraints
- 1 ≤ n ≤ 100,000 (number of inputs)
- 1 ≤ value < 10,000 (each number's value)
- Time limit: 1 second
