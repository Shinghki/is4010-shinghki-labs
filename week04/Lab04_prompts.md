# Lab 04 AI Interactions

## Problem 1: Finding common items
**Prompt:** I have two very large lists of product IDs. I need to find the common elements between them. Order does not matter. What is the most efficient Python data structure for this?
**AI Recommendation:** Set
**Reasoning:** Sets use hashing, allowing for O(1) average-time lookups. Using the set intersection operator (&) is significantly faster than nested loops in lists for large datasets.

## Problem 2: User profile lookup
**Prompt:** I need to look up user profiles by username frequently. Performance is critical. What's the most efficient data structure for this?
**AI Recommendation:** Dictionary
**Reasoning:** Dictionaries map keys (usernames) to values (profiles). This provides O(1) lookup speed, ensuring the application remains fast even as the number of users grows.

## Problem 3: Listing even numbers in order
**Prompt:** I need to filter a list for even numbers while keeping the original order. What approach should I take?
**AI Recommendation:** List (List Comprehension)
**Reasoning:** Lists are ordered sequences. Using a list comprehension allows for a concise, readable way to filter data while strictly maintaining the input sequence.