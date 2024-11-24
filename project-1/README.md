# Frequent Used Words

This project provides a Python class to find the most frequently used words in a given text. It demonstrates object-oriented programming practices and allows users to set the number of top frequently used words to retrieve.

## Features

- Process words from a text and count their occurrences.
- Retrieve the top `n` most frequently used words.
- Set the number of top words to retrieve (default is 10).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/-Tholokuhle-2024-/project-1.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project-1
    ```

## Usage

### Code

Here's an example of how to use the `FrequentWords` class:

```python
from collections import defaultdict, Counter
import heapq

class FrequentWords:
    def __init__(self, n=10):
        # Initialize with default top n words to 10
        self.n = n
        # Dictionary to store word counts
        self.word_count = defaultdict(int)
    
    def process_word(self, word):
        # Clean and normalize the word
        word = word.lower().strip(".,!?;:\"()[]")
        # Increment the count for the given word
        self.word_count[word] += 1
    
    def get_top_n_words(self):
        # Retrieve the top n words based on their frequency
        return heapq.nlargest(self.n, self.word_count.items(), key=lambda x: x[1])
    
    def set_n(self, n):
        # Allow user to set a different number of top words
        self.n = n

# Demonstration
text = "this is a test. This test is only a test."
# Split into words
words = text.split()

# Create an instance of FrequentWords
fw = FrequentWords()
# Process each word in the text
for word in words:
    fw.process_word(word)

# Get the top n words
top_words = fw.get_top_n_words()
print("Top words:", top_words)
```

### Steps to Run

1. **Initialize the Class**: Create an instance of the `FrequentWords` class.
    ```python
    fw = FrequentWords()
    ```
2. **Process Words**: Call the `process_word` method for each word in your text.
    ```python
    text = "your text here"
    words = text.split()
    for word in words:
        fw.process_word(word)
    ```
3. **Retrieve Top Words**: Call the `get_top_n_words` method to get the most frequently used words.
    ```python
    top_words = fw.get_top_n_words()
    print("Top words:", top_words)
    ```
4. **Sample Output**: For the input text = "This is a test. This test is only a test.", the output will be:
Top words: [('test', 3), ('this', 2), ('is', 2), ('a', 2), ('only', 1)]

4. **Set Number of Top Words**: Optionally, change the number of top words to retrieve using the `set_n` method.
    ```python
    fw.set_n(5)
    ```

## Customization

- **Change Default `n`**: You can change the default number of top words by passing a different value when initializing the class.
    ```python
    fw = FrequentWords(n=5)
    ```