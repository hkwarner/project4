from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self._dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self._dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self._dq)

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self._dq.push_back(val)

  def dequeue(self):
    # TODO replace pass with your implementation.
    return self._dq.pop_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
