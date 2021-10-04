import pprint
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
    def _assign_buckets(self, elements):
        for key, value in elements: #calculates the hash of each key
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size # positions the element in the bucket using hash
            self.buckets[index].append((key, value)) #adds a tuple in the bucket
    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    def __str__(self):
        return pprint.pformat(self.buckets) # pformat returns a printable representation of the object
if __name__ == "__main__":
     capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]
hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")
