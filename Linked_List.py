class Linked_List:

  class __Node:
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.__length = 0
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header

  def __len__(self):
    # return the number of value-containing nodes in
    # this list.
    # TODO replace pass with your implementation
    return self.__length

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    new = Linked_List.__Node(val)
    new.next = self.__trailer
    new.prev = self.__trailer.prev
    new.prev.next = new
    self.__trailer.prev = new
    self.__length += 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the
    # specified index. If the index is not a valid
    # position within the list, raise an IndexError
    # exception. This method cannot be used to add an
    # item at the tail position.
    # TODO replace pass with your implementation
    if index < 0 or index > self.__length - 1:
        raise IndexError("Invalid index for inserting into list.")
    cur = self.__header.next
    for i in range(index):
        cur = cur.next
    new = Linked_List.__Node(val)
    new.next = cur
    new.prev = cur.prev
    new.prev.next = new
    cur.prev = new
    self.__length += 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index < 0 or index > self.__length - 1:
        raise IndexError
    cur = self.__header.next
    for i in range(index):
        cur = cur.next
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    self.__length -= 1
    return cur.val

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation
    if index < 0 or index > self.__length - 1:
        raise IndexError
    cur = self.__header.next
    for i in range(index):
        cur = cur.next
    return cur.val

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    if(len(self) == 0):
        return
    cur = self.__header.next
    self.__header.next = cur.next
    cur.next.prev = self.__header
    cur.next = self.__trailer
    cur.prev = self.__trailer.prev
    cur.prev.next = cur
    self.__trailer.prev = cur

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    string = "[ "
    cur = self.__header.next
    for i in range(len(self)):
        sep = ", "
        if cur.next == self.__trailer:
            sep = " "
        string += str(cur.val) + sep
        cur = cur.next
    string += "]"
    return string

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_cur = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__iter_cur == self.__trailer:
        raise StopIteration
    to_return = self.__iter_cur.val
    self.__iter_cur = self.__iter_cur.next
    return to_return

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  ll = Linked_List()
  ll.rotate_left()
