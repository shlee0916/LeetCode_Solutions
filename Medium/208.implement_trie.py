'''
https://leetcode.com/problems/implement-trie-prefix-tree/description/
'''

class TrieNode:
    def __init__(self):
        self.word = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        
        node.word = True
            

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.child:
                return False
            node = node.child[ch]

        return node.word        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.child:
                return False
            node = node.child[ch]

        return True


if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert("apple")
    test1 = obj.search("apple")
    test2 = obj.startsWith("app")
    
    obj.insert("orange")
    test3 = obj.search("orange")
    test4 = obj.startsWith("or")
    
    test5 = obj.search("ale")
    test6 = obj.startsWith("oa")
    
    print(test1, True)
    assert test1 == True
    
    print(test2, True)
    assert test2 == True

    print(test3, True)
    assert test3 == True

    print(test4, True)
    assert test4 == True

    print(test5, False)
    assert test5 == False

    print(test6, False)
    assert test6 == False
