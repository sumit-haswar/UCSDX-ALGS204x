from typing import Dict, List

class TrieNode:
    def __init__(self, word: str=None):
        self.word = word
        self.children : Dict = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pass


    def generate(self, patterns: List[str]) -> TrieNode:
        for pattern in patterns:
            curr = self.root
            for idx, ch in enumerate(pattern):
                if ch in curr.children:
                    curr = curr.children[ch]
                else:
                    new_node = TrieNode(pattern[:idx + 1])
                    curr.children[ch] = new_node
                    curr = new_node

        return self.root


    def generate_from_text(self, text: str) -> TrieNode:
        pass
