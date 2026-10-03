text = """In 2026, we teach “intro-to-AI” with hands-on labs—no hype. Students ask: “Why tokens?”
Because models read pieces, not words. E.g., ‘ChatGPT-5’ ≠ ‘Chat’, ‘GPT’, ‘5’ in all schemes.
We track loss/accuracy, compare char/word/BPE, and test a URL: https://example.org/a/b?c=42.
Café prices rose 3.7%—blame supply-chain weirdness (and ☕ demand)."""
## Step 1 - Tokenize the text

import re

lower_text = text.lower()

clean_text = re.sub(r"[^\w\s]", " ", lower_text)

tokens = clean_text.split()

print(tokens)
print("Number of tokens:", len(tokens))
##step2 - Build a vocabulary

vocab = sorted(set(tokens))

stoi = {word: i for i, word in enumerate(vocab)}
itos = {i: word for word, i in stoi.items()}

##To inspect the vocabulary

print(vocab)
print("Vocabulary size:", len(vocab))
## STEP3- Numericalize the tokens

encoded = [stoi[word] for word in tokens]

print(encoded) ## for verification that everything is in integer
##Step4 - Decode the numerical indicies

decoded = [itos[i] for i in encoded]
print(decoded)

print(decoded == tokens)
##Step 5- Join the decoded tokens
decoded_text = " ".join(decoded)



print(decoded_text)
