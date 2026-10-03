import re

# Input text
text = """In 2026, we teach “intro-to-AI” with hands-on labs—no hype. Students ask: “Why tokens?”
Because models read pieces, not words. E.g., ‘ChatGPT-5’ ≠ ‘Chat’, ‘GPT’, ‘5’ in all schemes.
We track loss/accuracy, compare char/word/BPE, and test a URL: https://example.org/a/b?c=42.
Café prices rose 3.7%—blame supply-chain weirdness (and ☕ demand)."""

#Lowercase, remove punctuation, and split by whitespace
text = text.lower()
text = re.sub(r"[^\w\s]", " ", text)
tokens = text.split()

#Build vocabulary
word_to_id = {}
id_to_word = {}

for word in tokens:
    if word not in word_to_id:
        index = len(word_to_id)
        word_to_id[word] = index
        id_to_word[index] = word

#Convert words into numerical indices
encoded = []

for word in tokens:
    encoded.append(word_to_id[word])

#Convert numerical indices back into words
decoded = []

for index in encoded:
    decoded.append(id_to_word[index])

#  Join decoded words back into text
decoded_sentence = " ".join(decoded)

# Display results
print("Tokens:")
print(tokens)

print("\nTokenized length:", len(tokens))

print("\nVocabulary:")
print(word_to_id)

print("\nVocabulary size:", len(word_to_id))

print("\nNumericalized tokens:")
print(encoded)

print("\nDecoded tokens:")
print(decoded)

print("\nDecoded sentence:")
print(decoded_sentence)

print("\nSuccessfully decoded:", tokens == decoded)
