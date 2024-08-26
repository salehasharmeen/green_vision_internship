from collections import Counter

def bag_of_words(texts):
    vocab = set(word for text in texts for word in text.split())
    vocab = sorted(vocab)
    vocab_dict = {word: i for i, word in enumerate(vocab)}
    
    vectors = []
    for text in texts:
        vector = [0] * len(vocab)
        word_count = Counter(text.split())
        for word, count in word_count.items():
            if word in vocab_dict:
                vector[vocab_dict[word]] = count
        vectors.append(vector)
    
    return vocab_dict, vectors

texts = [
    "hello world",
    "hello from the other side",
    "world of Python"
]

vocab_dict, vectors = bag_of_words(texts)
print("Vocabulary Dictionary:", vocab_dict)
print("Numerical Vectors:")
for vector in vectors:
    print(vector)
