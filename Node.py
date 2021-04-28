class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
  def update(self):
    key, value = self.data 
    value+=1 
    self.data = (key,value)