import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        unique_words = set()
        for text in texts:
            unique_words.update(text.split())
            
        vocab = special_tokens + list(unique_words - set(special_tokens))
        
        self.word_to_id = {word: i for i, word in enumerate(vocab)}
        self.id_to_word = {i: word for i, word in enumerate(vocab)}
        self.vocab_size = len(vocab)
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        text = text.split()
        pre_encode_text = []
        
        for t in text:
            if t not in self.word_to_id:
                pre_encode_text.append("<UNK>")
            else:
                pre_encode_text.append(t)
        
        return [self.word_to_id[t] for t in pre_encode_text]
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        return " ".join([self.id_to_word[t] for t in ids])