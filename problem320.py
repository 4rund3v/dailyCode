"""
PROBLEM 320
Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

def distinct_character_window(word):
    window = ''
    visited_characters = []
    window_start = 0
    word_length = len(word)
    for index, char in enumerate(word):
        if char not in visited_characters:
            visited_characters.append(char)
            window = word[window_start:index]
        else:
            window_start = word.find(char, window_start)
    return window


if __name__ == "__main__":
    # Given word - jiujitsu 
    word = "jiujitsu"
    distinct_character_window = distinct_character_window(word)
    print(distinct_character_window)
