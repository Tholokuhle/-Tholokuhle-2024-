# Pangram Checker

This project provides a Python function to check whether a given string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once. This implementation assumes the input string does not contain any punctuation.

## Features

- Check if a string is a pangram.
- Remove spaces and convert the string to lowercase for accurate comparison.
- Use set operations to verify the presence of all alphabet characters.

## Installation

1. Clone the repository:
    git clone https://github.com/-Tholokuhle-2024-/project-3.git

2. Navigate to the project directory:
    cd project-3

## Usage

### Example Code

Here's an example of how to use the `ispangram` function:

```python
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    str1_set = set(str1)  # Create a set of all characters in the input string
    alphabet_set = set(alphabet)  # Create a set of all characters in the alphabet
    return alphabet_set.issubset(str1_set)  # Check if all alphabet characters are in the input string set

# Example usage
print(ispangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print(ispangram("Hello world"))  # Should return False
```

### Steps to Run

1. **Import the Function**: Ensure the `ispangram` function is defined in your script or imported from a module.
    ```python
    from pangram_checker import ispangram
    ```
2. **Check a String**: Call the `ispangram` function with the string you want to check.
    ```python
    result = ispangram("The quick brown fox jumps over the lazy dog")
    print(result)  # Should print True
    ```

## Customization

- **Change Alphabet**: You can check for pangrams in different alphabets by passing a different `alphabet` parameter.
    ```python
    custom_alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ispangram("Your custom string", alphabet=custom_alphabet)
    ```