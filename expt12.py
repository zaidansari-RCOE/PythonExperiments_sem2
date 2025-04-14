'''
Title: Extracting Words from Text File
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

import os

def extract_words_by_length(filename, lengths):
    """Reads a text file and prints words of specified lengths."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read the entire content of the file
            words = text.split()  # Split text into words
            
            # Remove punctuation marks around the words
            words = [word.strip('.,!?()[]{}":;') for word in words]

            # Initialize a dictionary to store words by length
            result = {length: [] for length in lengths}
            
            # Loop through each word and classify it based on length
            for word in words:
                word_length = len(word)
                if word_length in lengths:
                    result[word_length].append(word)
            
            # Print the results for each word length
            for length, words in result.items():
                if words:  # Only print lengths that have words
                    print(f"Words with {length} letters: {set(words)}")
                else:
                    print(f"No words with {length} letters.")
   
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = "sample.txt"  # Automatically using 'sample.txt'
    
    # Prompt the user to enter word lengths (comma-separated)
    lengths = list(map(int, input("Enter word lengths (comma-separated): ").split(',')))
    
    # Call the function to extract words based on the specified lengths
    extract_words_by_length(filename, lengths)

"""
Sample Output:

Enter word lengths (comma-separated): 3,4,5
Words with 3 letters: {'and', 'the', 'cat'}
Words with 4 letters: {'dogs', 'have'}
Words with 5 letters: {'house', 'quick'}

Enter word lengths (comma-separated): 6,7
No words with 6 letters.
Words with 7 letters: {'friends'}
"""
