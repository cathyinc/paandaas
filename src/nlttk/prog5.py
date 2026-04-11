def display5():
    code = '''import random
import hashlib
from itertools import combinations
documents={"D1":{"data","mining","machine","learning"},
           "D2":{"data","mining","deep","learning"},
           "D3":{"artificial","machine","neural","network"},
           "D4":{"data","science","machine","learning"}}
b=10
r=5
num_hashes=b*r
def jaccard(doc1,doc2):
    return len(doc1&doc2)/len(doc1|doc2)
max_val=1000
hash_functions=[(random.randint(1,max_val),random.randint(0,max_val))for _ in range(num_hashes)]
def minhash(document):
        signature=[]
        for a,b in hash_functions:
            min_value=float('inf')
            for word in documents:
                h=(a*hash(word)+b)%max_val
                min_value=min(min_value,h)
                signature.append(min_value)
        return signature
signatures={}
for doc_id,doc in documents.items():
    signatures[doc_id]=minhash(doc)
buckets={}
for doc_id,sig in signatures.items():
    for band in range(b):
        start=band*r
        end=start+r
        band_vector=tuple(sig[start:end])
        band_hash=hashlib.md5(str(band_vector).encode()).hexdigest()
        key=(band,band_hash)
        if key not in buckets:
            buckets[key]=[]
        buckets[key].append(doc_id)
candidate_pairs=set()
for bucket_docs in buckets.values():
    if len(bucket_docs)>1:
        for pair in combinations(bucket_docs,2):
            candidate_pairs.add(pair)
print("<......23BDA012......>")
print("similar documents:")
for d1,d2 in candidate_pairs:
    sim=jaccard(documents[d1],documents[d2])
    if sim>=0.5:
        print(f"{d1} and {d2}->similarity={sim:.2f}")'''
    print(code)
