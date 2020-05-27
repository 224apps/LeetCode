class WordNode:
    def __init__(self):
        self.children ={}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def search(self, word):
        self.res = False
        self.dfs(self.root, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isEndOfWord:
                self.res = True
            return 
        nextChar = word[0]
        if nextChar == ".":
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            if nextChar in node.children:
                self.dfs(node.children[nextChar], word[1:])
            