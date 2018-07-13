# Needed for Exercise 5
import random

# Exercise 1 - longest_word
def longest_word(word1, word2, word3):
    # Put all of the words into a list
    words = [word1, word2, word3]

    # Keep track of the longest word as we move through the list
    # Start it as the empty string, which is as short as a string gets, so
    # any word that gets passed in will be longer.
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

# Exercise 2 - reverse_string
def reverse_string(word):
    # Glad I Googled (or Bing'd!) this one.
    return ''.join(reversed(word))

# Exercise 3 - sum_to_n
def sum_to_n(n):
    if n < 0:
        print("I don't know how to sum to %s" % n)
    total = 0
    # I need to add one because by default range won't include the top number.
    for i in range(n + 1):
        total += i

    # But remember your math!
    # This is also equal to ((n * (n + 1)) / 2).
    return total

# Exercise 4 - is_triangle
def is_triangle(s1, s2, s3):
    # Check each pair of sides to make sure they are not shorter than the third
    # when combined.
    if s1 + s2 <= s3:
        return False
    if s1 + s3 <= s2:
        return False
    if s2 + s3 <= s1:
        return False
    # We checked all the pairs and everything looks good, we can return True.
    return True

# Exercise 5 - roll_dice
def roll_dice(num):
    total = 0
    # Inside Google, we use _ as a special variable name that communicates that
    # we are not going to use the value
    for _ in range(num):
        total += random.randint(1, 6)
    return total

# Extension #1 - isPrime
def isPrime(num):
    # Loop from 0 to (num - 1)
    # Check whether the remainder of dividing our number by each is 0
    # If it is, then we know our number isn't prime.
    for i in range(num):
        if i > 1 and num % i == 0:
            # As soon as I find a single factor for the number, I know it is not
            # Prime.
            return False
    return True

# Extension #2 - snake_case
def snake_case(word):
    snake_string = ""
    # I need to remember the staring index of the last string slice I used.
    last_index = 0
    # I want to loop over the indexes.
    for i in range(len(word)):
        # In JavaScript, we used string.charAt to find the character at an
        # index, so I Googled (or Bing'd!) "python charat" and found that I can
        # use brackets.
        character = word[i]
        # I also searched for "python is uppercase" and found that Python
        # strings have an "isupper" method that checks for me.
        if character.isupper():
            # Grab a slice from the last index I used to my current index.
            snake_string += word[last_index:i] + "_"
            # Then update my last_index
            last_index = i
    # Grab the last string slice
    snake_string += word[last_index:]
    # Also, everything should be lowercase.
    # A quick search tells me strings have a "lower" method that takes
    # uppercase strings and makes them lowercase.
    return snake_string.lower()

# Extension #3 - get_number_input
def get_number_input(prompt):
    # Do I have a valid value? Not yet!
    has_value = False
    # Keep asking until the user enters something valid.
    while not has_value:
        val = raw_input(prompt)
        # I might make changes to this variable, so make a copy so I will have
        # the original value to return to the user.
        test_val = val
        # Negative numbers should work, so let's check for the negative sign.
        if test_val[0:1] == "-":
            test_val = test_val[1:]
        # Searching for "python is number" led me to the string.isdigit method.
        if test_val.isdigit():
            # This only handles integer numbers, not ones with decimal points
            has_value = True
        if "." in test_val:
            # more Googling!
            index = test_val.index(".")
            if test_val[0:index].isdigit() and test_val[index+1:].isdigit():
                has_value = True

    # This works pretty well, but it still misses some valid types of numbers,
    # for example scientific notation (1e5). It's really hard to get a function
    # like this correct for every type of input your user could provide to you,
    # so when you can, use a library someone else has written!
    return val
