test_str = "hello world"
test_str_with_digits = "h3LL0 w0rld"

# Capitalize the first character of the string
capitalize_str = test_str.capitalize()
print(f"Oryginał:     '{test_str}'")
print(f"Duza litera:  '{capitalize_str}'")

# Check whether the string contains of letters and digits (isalnum() ==> isAlfaNumeric)
print(f'string "hello123"       zawiera same litery i cyfry:   {"hello123".isalnum()}      - TAK same litery i cyfry')
print(f'string "h3LL0w0rld"     zawiera same litery i cyfry:   {"h3LL0w0rld".isalnum()}    - TAK bez spacji')
print(f'string "h3LL0 w0rld"    zawiera same litery i cyfry:   {"h3LL0 w0rld".isalnum()}   - NIE bo spacja!')
print(f'string "hello-123"      zawiera same litery i cyfry:   {"hello-123".isalnum()}     - NIE bo myślnik!')
print(f'string "hello.123"      zawiera same litery i cyfry:   {"hello.123".isalnum()}     - NIE bo kropka!')

# Check whether all characters in the string are letters
isalpha()


# Check whether all characters in the string are digits
isdigit()


# Return the length of the string
len()


# Convert all uppercase letters in a string to lowercase
lower()


# Convert all lowercase letters in the string to uppercase
upper()


# Return the largest letter in the string
max()


# Return the smallest letter in the string
min()