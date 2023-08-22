class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = ""
        self.relevance = -1


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.counter=0
        self.res = []

    def insert(self, word):
        self.counter+=1
        dummyNode = self.root

        for letter in word:
            if letter not in dummyNode.children:
                dummyNode.children[letter] = TrieNode()
            
            dummyNode = dummyNode.children[letter]
        dummyNode.endOfWord = word
        dummyNode.relevance = self.counter

    def findAll(self, nodeDict):
        for value in nodeDict.values():
            if value.endOfWord:
                self.res.append((value.endOfWord, value.relevance))
            if value.children:
                self.findAll(value.children)
            
    def search(self, word):
        dummyNode = self.root

        for letter in word:
            if letter not in dummyNode.children:
                break
            
            dummyNode = dummyNode.children[letter]
        
        self.findAll(dummyNode.children)
        if self.res:
            self.res.sort(key=lambda x:x[1], reverse=True)
        
        print(self.res)

        return dummyNode.endOfWord == word
    

t = Trie()
t.insert("apple")
t.insert("banana")
t.insert("apricot")
t.insert("bamboo")
t.insert("duck")
t.insert("donut")
t.insert("april")
t.insert("apilog")
t.insert("applaud")
t.insert("aplex")
print(t.search("ap"))
