"""Python implementation of Binary Search Tree."""

class NodeDLL(object):
    """Node class for data storage."""

    def __init__(self, data=None, next_node=None, prev=None):
        """Initialize Node."""
        self.data = data
        self.next = next_node
        self.prev = prev

    def __repr__(self):
        """String representation."""
        return "Value: {}".format(self.data)


class DoubleLinkedList(object):
    """Double linked list impplementation.

    Methods supported
    push(val) - will insert the value (val) at the head of the list
    append(val) - will append the value (val) at the tail of the list
    pop() - will pop the first val off the head of the list and return it.
    shift() - will remove the last val from the tail of the list and return it.
    remove(val) - will remove the first instance of (val) found in the list,
    starting from the head.
    """

    def __init__(self, data=None):
        """Initialize list."""
        self.head = None
        self.tail = None
        self._length = 0
        try:
            for val in data:
                self.push(val)
        except TypeError:
            if data:
                self.push(data)

    def push(self, val):
        """Add val to the head of the list."""
        old_head = self.head
        self.head = NodeDLL(val, next_node=old_head)
        if old_head:
            old_head.prev = self.head
        if not self.tail:
            self.tail = self.head
        self._length += 1

    def pop(self):
        """Remove the val from the head of the list."""
        to_return = self.head
        if self._length < 1:
            raise IndexError('Cannot pop from an empty list.')

        new_head = self.head.next
        if new_head:
            new_head.prev = None
        self.head = new_head
        self._length -= 1
        if self._length < 1:
            self.tail = None
        return to_return.data

    def append(self, val):
        """Add val to the tail of the list."""
        old_tail = self.tail
        self.tail = NodeDLL(val, prev=old_tail)
        if old_tail:
            old_tail.next = self.tail
        if self._length < 1:
            self.head = self.tail
        self._length += 1

    def shift(self):
        """Remove the val from the tail of the list."""
        to_return = self.tail
        if self._length < 1:
            raise IndexError('Cannot shift from an empty list.')

        new_tail = self.tail.prev
        if new_tail:
            new_tail.next = None
        self.tail = new_tail
        self._length -= 1
        if self._length < 1:
            self.tail = None
        return to_return.data

    def remove(self, val):
        """Remove first occurance of val from list."""
        curr = self.head
        while curr:
            if curr.data is val:
                if self._length == 1:
                    self.head, self.tail = None, None
                elif curr is not self.head and curr is not self.tail:
                    curr.next.prev, curr.prev.next = curr.prev, curr.next
                elif curr is self.head:
                    self.head, curr.next.prev = curr.next, None
                elif curr is self.tail:
                    self.tail, curr.prev.next = curr.prev, None
                self._length -= 1
                return
            curr = curr.next

        raise ValueError('{} is not in the list'.format(val))

    def _repr(self):
        """Return list representation of dll."""
        l = []
        while True:
            try:
                popped_data = self.pop()
                l.append(popped_data)
            except IndexError:
                break
        return l

class Queue(object):
    """Implementation of Queue.

    This implementation supports the following public methods:
    enqueue(value): adds value to the queue
    dequeue(): removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)
    peek(): returns the next value in the queue without dequeueing it.
    If the queue is empty, returns None
    size(): return the size of the queue. Returns 0 if the queue is empty.
    """

    def __init__(self, data=None):
        """Initialize queue data structure."""
        self._container = DoubleLinkedList(data)

    def enqueue(self, val):
        """Add a value to the queue."""
        self._container.append(val)

    def dequeue(self):
        """Remove a value from the front of the queue."""
        return self._container.pop()

    def peek(self):
        """Return the next value in the queue without dequing it."""
        try:
            return self._container.head.data
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue."""
        return self._container._length

class Node(object):
    """Node, or leaf of the BST."""

    def __init__(self, val=None, parent=None):
        """Create node object."""
        self.val = val
        self.right = None
        self.left = None
        self.parent = parent
        self.height = 1

    def _is_leaf(self):
        """Return true if a leaf."""
        return not (self.right or self.left)

    def _is_interior(self):
        """Return true if a interior node."""
        return (self.right and self.left)

    def _onlychild(self):
        """Return string depending on children."""
        if self.left and not self.right:
            return 'left'
        if self.right and not self.left:
            return 'right'

    def _side(self):
        """Return if left or right child of parent."""
        if self.parent:
            return 'left' if self.parent.left == self else 'right'


class Bst(object):
    """Binary Search Tree.

    Binary Search tree supports the following methods:

    insert(val): will insert the value val into the BST. If val is
     already present, it will be ignored.

    search(val): will return the node containing that value, else None

    size(): will return the integer size of the BST (equal to the total
    no. of values stored in the tree). It will return 0 if the tree is empty.

    depth(): will return an integer representing the total number of
    levels in the tree. If there are no values, depth is 0, if one value the
    depth should be 1, if two values it will be 2, if three values it may be
    2 or 3, depending, etc.

    contains(val): will return True if val is in the BST, False if not.

    balance(): will return an integer, positive or negative that represents
    how well balanced the tree is. Trees which are higher on the left than
    the right should return a positive value, trees which are higher on the
    right than the left should return a negative value. An ideally-balanced
    tree should return 0.

    in_order(): return a generator that will return the values in the tree
    using in-order traversal, one at a time.

    pre_order(): return a generator that will return the values in the tree
    using pre-order traversal, one at a time.

    post_order(): return a generator that will return the values in the tree
    using post-order traversal, one at a time.

    breadth_first(): return a generator that will return the values in the tree
    using breadth frist traversal, one at a time.

    """

    def __init__(self, data=None):
        """Initialize tree."""
        self._size = 0
        self.root = None

        if data:
            for i in data:
                self.insert(i)

    def insert(self, val):
        """Insert val into BST. If val is already present will be ignored."""
        if not self.root:
            self.root = Node(val)
            self._size += 1
        else:
            self._step(val, self.root)

    def _step(self, val, curr):
        """Decide left or right and returns height."""
        if val < curr.val:
            curr = self._set_child(curr, 'left', val)
        elif val > curr.val:
            curr = self._set_child(curr, 'right', val)
        return curr.height

    def _set_child(self, curr, side, val):
        """Helping."""
        child = getattr(curr, side)
        if child:
            count = self._step(val, child)
            if curr.height <= count:
                curr.height += 1
        else:
            setattr(curr, side, Node(val, curr))
            self._size += 1
            if curr.height == 1:
                curr.height += 1
        return curr

    def search(self, val):
        """Return the node containing val."""
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

    def size(self):
        """Return the size of the BST."""
        return self._size

    def depth(self):
        """Return depth of the BST, representing total levels."""
        return 0 if not self.root else self.root.height

    def contains(self, val):
        """Return true if val is in the bst."""
        return self.search(val) is not None

    def balance(self, tree=None):
        """Return an integer of how well the tree is balanced.

        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        if not tree:
            tree = self.root
            if not tree:
                return 0

        leftbranch = 0 if not tree.left else tree.left.height
        rightbranch = 0 if not tree.right else tree.right.height

        return leftbranch - rightbranch

    def pre_order(self, node='root'):
        """Depth first pre-order traversal of tree."""
        if node == 'root':
            node = self.root

        if not node:
            return

        yield node.val

        for n in self.pre_order(node=node.left):
            yield n
        for n in self.pre_order(node=node.right):
            yield n

    def in_order(self, node='root'):
        """Depth first in-order traversal of tree."""
        if node == 'root':
            node = self.root

        if not node:
            return

        for n in self.in_order(node=node.left):
            yield n
        yield node.val
        for n in self.in_order(node=node.right):
            yield n

    def post_order(self, node='root'):
        """Depth frist post_order traversal of tree."""
        if node == 'root':
            node = self.root

        if not node:
            return

        for n in self.post_order(node=node.left):
            yield n
        for n in self.post_order(node=node.right):
            yield n
        yield node.val

    def breadth_first(self):
        """Breadth first traversal of tree."""
        q = Queue()
        q.enqueue(self.root)
        while q.peek():
            node = q.dequeue()
            yield node.val
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def delete(self, val):
        """Remove a node from the tree."""
        if self._size < 1 or not self.contains(val):
            return

        node = self.search(val)

        if node._is_leaf():  # no children
            if node.parent:
                setattr(node.parent, node._side(), None)
            else:
                self.root = None

        elif node._is_interior():  # two children
            next_node = self._find_replacement(node)
            self._size += 1
            self.delete(next_node.val)
            node.val = next_node.val

        else:  # one children
            child = getattr(node, node._onlychild())
            if node.parent:
                child.parent = node.parent
                setattr(node.parent, node._side(), child)
            else:
                self.root = child

        self._size -= 1

    def _find_replacement(self, node):
        """Find left most node of right subtree."""
        if node.right:
            return self._findmin(node.right)
        else:
            if node.parent:
                if node._side() == 'left':
                    return self.parent
                else:
                    node.parent.right = None
                    tmp = self._find_replacement(node.parent)
                    node.parent.right = node
                    return tmp

    def _findmin(self, node):
        """Find min of subtree, Min is always left most node."""
        while node.left:
            node = node.left
        return node
