from collections import defaultdict, Counter
import heapq

class FrequentWords:
    def __init__(self, n=10):       # Initialize with default top n words to 10
        self.n = n
        self.word_count = defaultdict(int)  # Dictionary to store word counts
    
    def process_word(self, word):
        word = word.lower().strip(".,!?;:\"()[]") 
        self.word_count[word] += 1        # Increment the count for the given word
    
    def get_top_n_words(self):
        return heapq.nlargest(self.n, self.word_count.items(), key=lambda x: x[1]) # Retrieve the top n words based on their frequency
    
    def set_n(self, n):
        self.n = n      # Allow user to set a different number of top words

#Demonstration
text = "this is a test. This test is only a test."
words = text.split()       # Split into words

fw = FrequentWords()      # Create an instance of FrequentWords
for word in words:          # Process each word in the text
    fw.process_word(word)

# Get the top n words
top_words = fw.get_top_n_words()
print("Top words:", top_words)