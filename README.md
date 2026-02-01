# Counting Bitstrings

This is a web demo for a project about counting the number of bitstrings that can be constructed while excluding one or more bit substrings. See the [code](counting_bitstrings/bitstring_graph.py) and [overview](static/overview.pdf) for more details!

## What does counting bitstrings mean?

A bitstring is a series of ones and zeroes, like 101101011 or 10001001. The aim of this project was to figure out how many ways you could construct a bitstring of length n while excluding a certain pattern of ones and zeroes. For example, the number of ways to construct a bitstring of length 3 while excluding 00 is 5 -- 010, 011, 101, 110, and 111. The other 3 valid bitstrings of length 3, 000, 001, and 100, are not counted since they include 00.

## What did we find out?

More details on our process are coming soon, but, to put it simply, we represented the construction of a bitstring as a directed graph of k-1 bit suffixes where k is the length of the longest restriction. Traversing an edge -- going from one suffix to another -- is equivalent to adding one bit to the end of the bitstring you're constructing. Here's an example of a graph where the restriction is 000:

<img width="796" height="598" alt="image" src="https://github.com/user-attachments/assets/abcb304a-163b-4d78-9f62-6c2a19f925f4" />

As you can see, there is a path from 01 to 10 because 010 is a valid bitstring, but there is no path from 00 back to 00 because 000 is not valid. We found that the adjacency matrix of this graph can be used to find how many bitstrings of length n can be constructed. If we have an adjacency matrix A, the number of possible bitstrings of length n that can be constructed with the restrictions represented in the graph is the sum of A^n-m+1, where m is the longest restriction. More details on this math can be found in the [code](counting_bitstrings/bitstring_graph.py)! 
