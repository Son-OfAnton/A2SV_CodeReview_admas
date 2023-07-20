import sys

def search_word_in_news(word, file_path="../news.txt"):
    """
    Search for a word in a news file and print the paragraphs containing the word.

    Parameters:
        word (str): The word to search for (case insensitive).
        file_path (str): The path to the news file. Default is "../news.txt".

    Raises:
        FileNotFoundError: If the news file is not found.
        Exception: If any other unexpected error occurs.

    Note:
        The function reads the specified news file line by line.
        It checks if the word is present in any line (case insensitive).
        If found, it prints the paragraph containing the word along with the two next paragraphs.

    Example:
        search_word_in_news("technology", "my_news.txt")  # Search for "technology" in "my_news.txt".
        search_word_in_news("apple")  # Search for "apple" in the default file "../news.txt".
    """
    try:
        found = False
        with open(file_path, "r") as file:
            for line in file:
                # Check if the word is in the line (case insensitive)
                if word.lower() in line.lower():
                    found = True
                    # Print the paragraph containing the word and the two next paragraphs
                    print(line.strip())
                    print(file.readline().strip())
                    print(file.readline().strip())
                    break

        if not found:
            print(f"The word '{word}' was not found in the news file.", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: News file '{file_path}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

search_word_in_news("technology", "my_news.txt")
