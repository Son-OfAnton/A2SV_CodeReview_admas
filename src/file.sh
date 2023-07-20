#!/bin/bash

echo -n "Enter a word to search for: "
read word

# Use grep to search for the word in the news.txt file
paragraph=$(grep -i -m 1 -B 1 -A 1 "$word" ../news.txt)

# Check if the word was found
if [ -n "$paragraph" ]; then
    # Print the paragraph containing the word
    echo "$paragraph"
else
    echo "The word '$word' was not found in the news file."
fi
