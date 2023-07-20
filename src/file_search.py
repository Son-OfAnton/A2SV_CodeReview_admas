import sys

word = input("Enter a word to search for: ")

with open("../news.txt", "r") as file:
    for line in file:
        # Check if the word is in the line (case insensitive)
        if word.lower() in line.lower():
            # Print the paragraph containing the word
            print(line.strip())
            print(file.readline().strip())
            print(file.readline().strip())
            break
    else:
        print(f"The word '{word}' was not found in the news file.", file=sys.stderr)
