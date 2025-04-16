# Sample Program: String Functions in Python

# Original string
text = "  Hello, Python World!  "

# 1. strip() - removes leading and trailing whitespaces
cleaned_text = text.strip()
print("1. Stripped text:", cleaned_text)

# 2. lower() - converts string to lowercase
print("2. Lowercase:", cleaned_text.lower())

# 3. upper() - converts string to uppercase
print("3. Uppercase:", cleaned_text.upper())

# 4. replace() - replaces a substring with another
replaced_text = cleaned_text.replace("Python", "Coding")
print("4. Replaced text:", replaced_text)

# 5. split() - splits the string into a list
words = cleaned_text.split()
print("5. Split into words:", words)

# 6. join() - joins a list into a string
joined_text = "-".join(words)
print("6. Joined with hyphens:", joined_text)

# 7. find() - returns the index of first occurrence
index = cleaned_text.find("World")
print("7. Index of 'World':", index)

# 8. count() - counts how many times a substring appears
count = cleaned_text.count("o")
print("8. Count of 'o':", count)

# 9. isalpha() - checks if all characters are letters
print("9. Is 'Hello' alphabetic?", "Hello".isalpha())

# 10. startswith() / endswith()
print("10. Starts with 'Hello'? ", cleaned_text.startswith("Hello"))
print("11. Ends with 'World!'? ", cleaned_text.endswith("World!"))
