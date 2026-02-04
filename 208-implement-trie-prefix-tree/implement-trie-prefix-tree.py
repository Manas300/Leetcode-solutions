# A single Trie node
class TrieNode:
    def __init__(self):
        # Dictionary to hold child nodes (char -> TrieNode)
        self.children = {}
        # Flag to indicate if a word ends at this node
        self.is_end = False

class Trie:

    def __init__(self):
        # Root node doesn't hold any character
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for char in word:
            # If the character path doesn't exist, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word exists in the Trie, else False.
        """
        node = self.root
        for char in word:
            # If character is missing, word doesn't exist
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # Return True only if this node marks the end of a word
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the Trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            # If character path doesn't exist, prefix not found
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # All characters in prefix found
        return True