# How to implement the cache of size 10?
# How you invalidate the cache?

import time

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

    def get(self, key: str) -> int:
        """
        Get data from cache, if exists.
        """
        val = self.cache.get(key, False)
        if val:
            self.cache_usage[key] = self.cache_usage.get(key, 0) + 1
            print(f"Cache usage: {self.cache_usage}")
            return val
        else:
            return False

    def put(self, key, value):
        """
        Put data for storing in cache.
        """
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

def slow_read_from_disk(key: str) -> int:
    """
    Emulation of the slow reading from a disk.
    """
    data_on_disc = {
        "table": 3,
        "spoon": 1,
        "chair": 2,
        "pen": 5
    }
    time.sleep(2)

    return data_on_disc.get(key, False)

def get_data(key: str, cache: Cache) -> int:
    """
    Returns data from disk or from cache, is exists.
    """
    t = time.perf_counter()
    val = cache.get(key)
    if val:
        print(f"Elapsed time cache: {time.perf_counter() - t:.4f}")
        return val
    else:
        val = slow_read_from_disk(key)
        if val:
            cache.put(key, val)
            print(f"Elapsed time disk: {time.perf_counter() - t:.4f}")
            return val
        else:
            return False


cache = Cache(3)
### simple example
# t = time.perf_counter()

# print(get_data("table", cache))
# print(get_data("table", cache))
# print(get_data("spoon", cache))
# print(get_data("chair", cache))
# print(get_data("pen", cache))

# print(f"Full elapsed time: {time.perf_counter() - t:.4f}")

### user interaction example with the feeling of performance

while True:
    user_input = input("Type your object...\n")
    if user_input == "exit":
        break
    else:
        val = get_data(user_input, cache)
        if val:
            print(val)
        else:
            print("No such value!")
