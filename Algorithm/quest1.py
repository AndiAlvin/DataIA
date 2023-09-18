def hitung_kemunculan(DATA, QUERIES):
    kemunculan = {query: DATA.count(query) for query in QUERIES}
    hasil = [kemunculan.get(query, 0) for query in QUERIES]
    return hasil

DATA = ['apple', 'banana', 'cherry', 'banana', 'apple']
QUERIES = ['apple', 'banana', 'grape']

output = hitung_kemunculan(DATA, QUERIES)
print(output)  # Output: [2, 2, 0]
