# Sejuti Mannan
# NYU Tandon Data Science Bootcamp
# Week 1 (10/2) Introduction to Bootcamp and Python Fundamentals HW

'''
1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
2. Iterate through the following list of animals and print each one in all caps.

  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
'''

# Question 1
def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    return vowel_count


# Question 2
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

# Question 3
def odd_or_even():
    num = 1
    while num <= 20:
        if (num % 2) == 0:
            print(num, "even ")
        else:
            print(num, "odd ")

        num += 1

# Question 4
def sum_of_integers(a, b):
    return a + b
