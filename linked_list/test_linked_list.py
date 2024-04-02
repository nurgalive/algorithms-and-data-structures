from linked_list import LinkedList

def test_create_linked_list():
    assert LinkedList(["a"]) is not None

def test_iterate_over_linked_list():
    for obj in LinkedList(["a", "b", "c"]):
        print(obj)

# add text fixture
#         import pytest

# # ...

# @pytest.fixture
# def hash_table():
#     sample_data = HashTable(capacity=100)
#     sample_data["hola"] = "hello"
#     sample_data[98.6] = 37
#     sample_data[False] = True
#     return sample_data

# def test_should_find_value_by_key(hash_table):
#     assert hash_table["hola"] == "hello"
#     assert hash_table[98.6] == 37
#     assert hash_table[False] is True