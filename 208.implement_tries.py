class Trie(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.child = {}
            self.is_end_of_word = False

        def has_child(self, val):
            return val in self.child.keys()

    def __init__(self):
        self.root = self.Node(" ")

    def add_child(self, node, val):
        node.child[val] = self.Node(val)

    def get_child(self, node, val):
        return node.child[val]

    def insert(self, word):
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
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if current.has_child(char):
                current = self.get_child(current, char)
            else:
                return None
        return current.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if current.has_child(char):
                current = self.get_child(current, char)
            else:
                return None
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
