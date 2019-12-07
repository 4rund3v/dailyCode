'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''


class CharTree(object):
    """
       build a tree where the first character is the root node
       from there on each character becomes a child node
    """
    def __init__(self, char):
        self.char = char
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)


def build_tree(tree, word):
    if not tree.char == word[0]:
        print('not matching chars')
        return
    def process_tree(node, ch):
        print('processing : {}'.format(ch))
        print('Node : {}'.format(node.char))
        cnode = None
        if not node.children:
            cnode = CharTree(ch)
            node.add_child(cnode)
        else:
            for child in node.children:
                if child.char == ch:
                    cnode = child
                    break
            else:
                cnode = CharTree(ch)
                node.add_child(cnode)
        return cnode
    temp = tree
    for ch in word[1:]:
        temp = process_tree(temp, ch)

def print_possibilites(chars):
    global tree_map
    possibilites = []
    def get_possibilites(node, ch):
        pass
    #TODO!!
    for ch in chars:
        get_possibilites(ch)        
    return



if __name__ == '__main__':
    words = ['doom', 'dingy', 'booom', 'yay', 'sad', 'wew', 'booda', 'bonda', 'saphire']
    tree_map = {}
    for word in words:
        if not tree_map.has_key(word[0]):
            tree_map[word[0]] = CharTree(word[0])
        temp_tree = tree_map[word[0]]
        print('Word : {} --> temp_tree : {}'.format(word, temp_tree.char))
        build_tree(temp_tree, word)
    char_str = ''
    while True:
        print('Press  cntrl c to quit')
        print('Enter a key and press enter to see possibilites')
        _str = raw_input('---> : ')
        print('\n \n Possibilites are ')
        char_str += _str.strip()
        print_possibilites(char_str)
    print('Done !')
