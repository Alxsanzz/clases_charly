# STRINGS IN PYTHON
"""
    Alexis Adhemar Covarrubias Sanchez
    2630026
    IM 1-1
"""
# EXECUTIVE SUMMARY

"""
    A string is a sequence of characters represented by the str data type in Python. Strings are immutable, which means they
    cannot be changed directly after they are created. Python allows us to concatenate, search, replace, split, and
    format strings, as well as obtain their length and extract substrings using slicing. Validating and normalizing 
    text helps prevent incorrect input. Methods such as strip() and lower() make text easier to compare.

    This assignment contains six problems involving string methods, input validation, and text processing. 
    Each problem includes its description, inputs, outputs, validations, and three test cases.
"""


"""
    - Strings are immutable; operations create new strings
    - Use strip() and lower() to normalize text when appropriate
    - Explain slice indexes instead of using unexplained numbers
    - Prefer built-in string methods whenever possible
    - Check for empty input before validating its format
    - Use clear variable names and understandable error messages
"""







# PROBLEM 1: "FULL NAME FORMATTER"

# Description:
# Normalize a full name, format it in title case, and display the initials of each word

# Inputs:
# - full_name: a string containing a person's full name

# Outputs:
# - Formatted namE
# - Initials

# Validations:
# - The name cannot be empty
# - At least two words are required

# Test cases:
# 1) Normal: "alexis covarrubias sanchez" -> "Alexis Covarrubias Sanchez"
#    Initials: "A.C.S."

# 2) Border: "  FATIMA MORALES  " -> "Fatima Morales"
#    Initials: "F.M."

# 3) Error: "   " -> Error: name cannot be empty



full_name = input("Enter your full name: ").strip()
name_parts = full_name.split()

if not full_name:
    print("Error: name cannot be empty")

elif len(name_parts) < 2:
    print("Error: enter at least two words")

else:
    formatted_name = " ".join(name_parts).title()
    initials = "".join(part[0].upper() + "." for part in name_parts)

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")



# PROBLEM 2: SIMPLE EMAIL VALIDATOR

# Description:
# Validate the basic structure of an email address
# If it is valid, display its domain

# Inputs:
# email_text: a string containing an email address

# Outputs:
# Valid email: true or false
# Domain, if the email is valid

# Validations:
# The email cannot be empty
# It must contain exactly one '@'
# It cannot contain spaces
# The domain must contain a dot
# The local part and domain cannot be empty

# Test cases:
# 1) Normal: "alexis@gmail.com" -> valid
#    Domain: "gmail.com"

# 2) Border: "a@g.co" -> valid
#    Domain: "g.co"

# 3) Error: "alexis gmail.com" -> invalid



email_text = input("Enter an email: ").strip()

if email_text.count("@") == 1 and " " not in email_text:
    domain = email_text.split("@")[1]

    if "." in domain and not domain.startswith(".") and not domain.endswith("."):
        print("Valid email: true")
        print(f"Domain: {domain}")
    else:
        print("Valid email: false")
else:
    print("Valid email: false")




# PROBLEM 3: PALINDROME CHECKER

# Description:
# Determine whether a phrase reads the same forward and backward, ignoring spaces and letter case

# Inputs:
# - phrase: a phrase to check

# Outputs:
# - Whether the phrase is a palindrome and its normalized form

# Validations:
# - Input must not be empty after strip()
# - At least three non-space characters are required

# Test cases:
# 1) Normal: "Sator Rotas" -> true
# 2) Border: "Oso" -> true
# 3) Error: " a " -> error message

phrase = input("Enter a phrase: ").strip()

if not phrase:
    print("Error: phrase cannot be empty")
else:
    normalized_phrase = "".join(phrase.lower().split())

    if len(normalized_phrase) < 3:
        print("Error: enter at least three non-space characters")
    else:
        is_palindrome = normalized_phrase == normalized_phrase[::-1]
        print(f"Normalized phrase: {normalized_phrase}")
        print(f"Is palindrome: {str(is_palindrome).lower()}")



# PROBLEM 4: SENTENCE WORD STATISTICS

# Description:
# Count the words in a sentence and display the first, last, shortest, and longest words

# Inputs:
# - sentence: a sentence containing one or more words

# Outputs:
# - Word count, first word, last word, shortest word, longest word

# Validations:
# - Input must not be empty after strip()
# - At least one word must remain after split()
#
# Test cases:
# 1) Normal: "Hola me llamo Alexis" -> count 4, first Hola, last Alexis

# 2) Border: "  Hola   " -> count 1, first/last/shortest/longest Hola

# 3) Error: "   " -> error message



sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: sentence cannot be empty")
else:
    words = sentence.split()

    shortest = words[0]
    longest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word

    print("Word count:", len(words))
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Shortest word:", shortest)
    print("Longest word:", longest)



# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER

# Description:
# Classify a password as weak, medium, or strong using simple rules

# Inputs:
# - password_input: a password string

# Outputs:
# - Password strength: weak, medium, or strong

# Validations:
# - Password must not be empty
# - Strength is based on length and character types

# Test cases:
# 1) Normal: "AJHSjagda67@" -> strong

# 2) Border: "Abcdefgh" -> medium

# 3) Error: "" -> error message



password = input("Enter a password: ")

if not password:
    print("Error: password cannot be empty")
else:
    upper = False
    lower = False
    number = False
    symbol = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            number = True
        else:
            symbol = True

    if len(password) < 8:
        print("Password strength: weak")
    elif upper and lower and number and symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")



# Problem 6: Product Label Formatter

# Description:
# Create a product label exactly 30 characters long. Short labels are padded with spaces and long labels are truncated

# Inputs:
# - product_name: a product name
# - price_value: a positive numeric price

# Outputs:
# - A label containing the product name and price, exactly 30 characters

# Validations:
# - Product name must not be empty after strip()
# - Price must be numeric and greater than zero

# Test cases:
# 1) Normal: "Laptop", "25.50" -> a 30-character label

# 2) Border: "Mouse", "1" -> padded to 30 characters

# 3) Error: "Auriculars", "abc" -> error message



product_name = input("Enter product name: ").strip()

if not product_name:
    print("Error: product name cannot be empty")
else:
    try:
        price = float(input("Enter product price: "))

        if price <= 0:
            print("Error: price must be positive")
        else:
            label = f"Product: {product_name} | ${price:.2f}"
            label = label[:30].ljust(30)

            print("Label:", label)
            print("Label length:", len(label))

    except ValueError:
        print("Error: price must be a number")


# CONCLUSIONS

"""
    In this assignment, i learned how to work with strings in Python. I used methods to change, compare, and separate text.
    I also learned how to validate user input. These exercises helped me understand how strings work
    and how they can be used in simple programs
"""

# REFERENCES
# 1. Python Software Foundation. Built-in Types
# https://docs.python.org/3/library/stdtypes.html

# 2. Python Software Foundation. Built-in Functions
# https://docs.python.org/3/library/functions.html

# 3. Python Software Foundation. Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# 4. Python Software Foundation. An Informal Introduction to Python
# https://docs.python.org/3/tutorial/introduction.html

# 5. Python Software Foundation. Input and Output
# https://docs.python.org/3/tutorial/inputoutput.html
