from LinkedList import LinkedList
from Node import Node

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    linkedLists=[]
    for elem in range(size):
        linkedLists.append(LinkedList())
    return linkedLists

  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  # If it finds the given key in the table, it will return (True, index)
  # If not, it will return (False, the index where it would be inserted)
  def hash_func(self, key):
    hash1 = hash(key)
    m = len(self.arr)
    index = hash1 % m 

    return index
  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    index = self.hash_func(key)
    item=0
    val = self.arr[index].find(key)
    if val != -1:
      item = self.arr[index].update_val(key, val) 
    if item != -1:
      self.arr[index].append([key,value])

    # At this point, we'll know that the given key doesn't exist
    # in the table yet, and that result[1] is the index
    # where the new key-value pair should be inserted.

  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for LinkedList in self.arr:
        #each element of hash table is a Linked List, which has a key value pair
      print(LinkedList.print_nodes())



