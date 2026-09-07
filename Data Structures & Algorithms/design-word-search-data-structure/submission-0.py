class node :
    def __init__(self):
        self.children = dict()
        self.is_word_end = False

class WordDictionary:


    def __init__(self):
        self.root = node()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = node()
            curr_node = curr_node.children[c]
        curr_node.is_word_end = True
        return None

    def search(self, word: str) -> bool:
        curr_node = self.root
        
        def dfs(i,curr_node):
            if i == len(word):
                return curr_node.is_word_end

            c = word[i]

            if c==".":
                for child in curr_node.children.values():
                    if dfs(i+1,child):
                        return True
                return False 

            if c not in curr_node.children:
                return False

            return dfs(i+1,curr_node.children[c])
        return dfs(0,curr_node)

