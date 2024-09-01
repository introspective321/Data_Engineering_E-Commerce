class HashTable:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.table = [None] * num_buckets

    def custom_hash_function(self, key):
        common_alphabets = "BAI"
        hash_value = 0
        for char in key:
            if char in common_alphabets:
                hash_value = (hash_value * 31 + ord(char)) % self.num_buckets
            else:
                hash_value = (hash_value * 37 + ord(char)) % self.num_buckets
        return hash_value

    def insert(self, key, value):
        index = self.custom_hash_function(key)
        start_index = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.num_buckets
            if index == start_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.custom_hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.num_buckets
            if index == start_index:
                return None
        return None

# Create a hash table with 10 buckets
hash_table = HashTable(10)

# Insert some key-value pairs
hash_table.insert('Artwork1', 'Painting')
hash_table.insert('Artwork15', 'Sculpture')
hash_table.insert('Artwork3', 'Drawing')

keys = ['Artwork1', 'Artwork15', 'Artwork3']
for key in keys:
    bucket = hash_table.custom_hash_function(key)
    print(f"Key: {key} is mapped to bucket: {bucket}")

# Search for keys
print(hash_table.search('Artwork1'))  # Output: Painting
print(hash_table.search('Artwork15')) # Output: Sculpture
print(hash_table.search('Artwork2'))  # Output: None (not found)





