# How to implement the cache of size 10?
# How you invalidate the cache?


# TODO: make the cache estimate the size of the stored objects
class Cache:
    """
    Simple cache.
    """

    def __init__(self, cache_size) -> None:
        self.cache_size = cache_size
        self.cache = {}
        self.cache_usage: dict[str, int] = {}
        print(f"Created cache with size: {self.cache_size}")

    def get_from_cache(self, key: str) -> str:
        self.cache_usage[key] = self.cache_usage.get(key, 0) + 1
        print(f"Cache usage: {self.cache_usage}")
        return self.cache.get(key, "No value saved in cache")

    def add_to_cache(self, key, value):
        if len(self.cache_usage) == self.cache_size:
            print("Cache is full.")
            self.cache_usage = dict(sorted(self.cache_usage.items(), key=lambda x: x[1], reverse=True))
            object_to_delete = self.cache_usage.popitem()  # popitem returns the last object from dict (key, value)
            print(f"Deleting: '{object_to_delete}'")
            del self.cache[object_to_delete[0]]
        self.cache[key] = value
        self.cache_usage[key] = 0
        print(f"Cache: {self.cache}")
        print(f"Cache usage: {self.cache_usage}")



cache = Cache(3)
print(cache.get_from_cache("table"))
cache.add_to_cache("table", 3)
print(cache.get_from_cache("table"))
cache.add_to_cache("spoon", 1)
cache.add_to_cache("chair", 2)
cache.add_to_cache("pen", 5)
