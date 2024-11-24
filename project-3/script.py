import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    str1_set = set(str1)  # Create a set of all characters in the input string
    alphabet_set = set(alphabet)  # Create a set of all characters in the alphabet
    return alphabet_set.issubset(str1_set)  # Check if all alphabet characters are in the input string set

# Example usage
print(ispangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print(ispangram("Hello world"))  # Should return False