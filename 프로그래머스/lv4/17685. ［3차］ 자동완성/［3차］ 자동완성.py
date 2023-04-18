class Node:
    def __init__(self, word = ''):
        self.word = word
        self.cnt = 1
        self.childnode = {}
        
class Trie:
    def __init__(self):
        self.root = Node()
        
        
    def insert(self, word):
        node = self.root
        node.cnt += 1
        control = True
        for char in word:
            if char in node.childnode:
                node.childnode[char].cnt += 1
                node = node.childnode[char]
                
            else:
                newnode = Node(char)
                node.childnode[char] = newnode
                node = newnode
                
    def find(self, word):
        node = self.root
        result = 0
        for char in word:
            if char in node.childnode and node.childnode[char].cnt > 1:
                node = node.childnode[char]
                result += 1
            else:
                result += 1
                break
        
        return result
                

def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.find(word)
    return answer