def custom_hash_function(key, num_buckets):
    
    """
    Custom hash function for the 'Artwork Listings' table.
    
    Parameters:
    key (str): The key to hash, typically a unique identifier for artwork.
    num_buckets (int): The number of hash buckets to distribute data.
    
    Returns:
    int: The index of the bucket where the data should be stored.
    """
    # Define common alphabets from the roll numbers
    common_alphabets = "BAI"

    # Initialize hash value
    hash_value = 0

    # Process each character in the key
    for char in key:
        if char in common_alphabets:
            # Simple hash calculation considering common alphabets
            hash_value = (hash_value * 31 + ord(char)) % num_buckets
        else:
            # Hash calculation for other characters
            hash_value = (hash_value * 37 + ord(char)) % num_buckets

    return hash_value

# Example usage
num_buckets = 10  # Number of hash buckets
keys = ['Artwork1', 'Artwork15', 'Artwork3']

for key in keys:
    bucket = custom_hash_function(key, num_buckets)
    print(f"Key: {key} is mapped to bucket: {bucket}")
