class WordDictionary(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.child = {}
            self.is_end_of_word = False

        def has_child(self, val):
            return val in self.child.keys()

        def get_all_child(self):
            return self.child.values()

        def has_any_child(self):
            return len(self.child) > 0

    def __init__(self):
        self.root = self.Node(" ")

    def add_child(self, node, val):
        node.child[val] = self.Node(val)

    def get_child(self, node, val):
        return node.child[val]

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            if not current.has_child(char):
                self.add_child(current, char)
            current = self.get_child(current, char)
        current.is_end_of_word = True

    def search(self, word):
        return self._search(word, self.root)

    def _search(self, word, parent_node):
        """
        :type word: str
        :rtype: bool
        """
        current = parent_node
        for ind, char in enumerate(word):
            if char == ".":
                if not current.has_any_child():
                    return False
                results = []
                for child in current.get_all_child():
                    val = child.val
                    res = self._search(child.val + word[ind + 1 :], current)
                    results.append(res)
                    if res:
                        child_current = self.get_child(current, val)
                if not bool(sum(results)):
                    return False
                else:
                    current = child_current
            elif current.has_child(char):
                current = self.get_child(current, char)
            else:
                return False
        return current.is_end_of_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
