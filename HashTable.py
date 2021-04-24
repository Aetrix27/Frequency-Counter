from LinkedList import LinkedList

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

  def hash_func(self, key):
    #dont need testmode
    hash1 = hash(key)
    m = len(self.arr)
    index = hash1 % m # initial_i's range: [0, m - 1] (inclusive)

    if self.arr[index] == 1: 
        return (True, index)
        print((True, index))

    elif self.arr[index] == key:
        return (False, index)
        print((False, index))

    hash2 = hash(key + ord('d'))

    c = hash2 % (m - 1) + 1
    i = (index + c) % m

  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
        #LinkedList.head = result
    print(key)
    for i in self.arr:
        #result = i.find(key)
        #if result == None:
        i.data = key
        print(key)


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for elem in self.arr:
        #each element of hash table is a Linked List, which has a key value pair
        print(elem.print_nodes())



