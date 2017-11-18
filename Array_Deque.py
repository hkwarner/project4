from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__size = 0
    self.__front = 0

  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    string ="[ "
    for i in range(self.__front, self.__front + self.__size):
        string += str(self.__contents[i % self.__capacity])
        if i != self.__front + self.__size - 1:
            string += ","
        string += " "
    string += "]"
    return string

  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity *= 2
    new = [None] * self.__capacity
    cur = self.__front
    for i in range(self.__size):
        new[i] = self.__contents[cur]
        cur = (cur + 1) % self.__size
    self.__contents = new
    self.__front = 0

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
        self.__grow()
    self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1

  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
        return
    val = self.__contents[self.__front]
    self.__front = (self.__front + 1) % self.__capacity
    self.__size -= 1
    return val

  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
        return
    return self.__contents[self.__front]

  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
        self.__grow()
    self.__contents[(self.__front + self.__size) % self.__capacity] = val
    self.__size += 1

  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
        return
    val = self.__contents[(self.__front + self.__size - 1) % self.__capacity]
    self.__size -= 1
    return val

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
        return
    return self.__contents[(self.__front + self.__size - 1) % self.__capacity]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
