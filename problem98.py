"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
 are those horizontally or vertically neighboring.
  The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

def solution(charcter_board, search_word):
    def check_if_pattern_exists():
        return
    
    return True

if __name__ == '__main__' :
    charcter_board = []
    charcter_board.append(['A','B','C','E'])
    charcter_board.append(['S','F','C','S']) 
    charcter_board.append(['A','D','E','E'])
    search_word = 'ABCCED'
    print(solution(charcter_board, search_word))
