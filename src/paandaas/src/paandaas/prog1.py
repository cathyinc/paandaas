def display(1):
    print(1)

import math

docs = {
    "Good Boy",
    "Good Girl",
    "Boy Girl Good"
}

word = input("Enter the word: ").lower()
N = len(docs)

def mapper_tf(doc):
    words = doc.lower().split()
    return words.count(word), len(words)

tf_values = []

for doc in docs:
    count, total = mapper_tf(doc)
    tf_values.append(count / total)

def mapper_df(doc):
    return 1 if word in doc.lower().split() else 0

df = sum(mapper_df(doc) for doc in docs)

idf = math.log10(N / df) if df > 0 else 0

tfidf_values = [tf * idf for tf in tf_values]

print("TF (Term Frequency):", tf_values)
print("DF (Document Frequency):", df)
print("IDF (Inverse Document Frequency):", idf)
print("TF-IDF:", tfidf_values)
