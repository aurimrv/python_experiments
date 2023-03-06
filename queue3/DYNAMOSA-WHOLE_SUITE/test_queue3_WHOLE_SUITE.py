#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue3/WHOLE_SUITE/test_queue3.py.orig
import pytest
import queue3 as module_0

def test_case_0():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    none_type_0 = None
    dict_0 = {queue_0: queue_0, none_type_0: queue_0, str_0: queue_0}
    none_type_1 = queue_0.enqueue(dict_0)
    var_0 = doubly_linked_list_0.getTail()
    bool_0 = doubly_linked_list_0.isEmpty()
    assert bool_0 is True
    none_type_2 = queue_0.enqueue(none_type_0)
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 0
    bool_1 = doubly_linked_list_0.isEmpty()
    assert bool_1 is True
    var_1 = queue_0.getTail()
    var_2 = queue_0.dequeue()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.Node'
    assert f'{type(var_2.value).__module__}.{type(var_2.value).__qualname__}' == 'builtins.dict'
    assert len(var_2.value) == 3
    assert var_2.next is None
    assert var_2.prev is None

def test_case_1():
    queue_0 = module_0.Queue()
    str_0 = '\x0c{xK\\BR?w'
    queue_1 = module_0.Queue()
    var_0 = queue_0.getHead()
    bool_0 = queue_1.isEmpty()
    assert bool_0 is True
    none_type_0 = None
    none_type_1 = queue_1.enqueue(none_type_0)
    none_type_2 = queue_0.enqueue(queue_1)
    var_1 = queue_1.dequeue()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert var_1.value is None
    assert var_1.next is None
    assert var_1.prev is None

def test_case_2():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    queue_1 = module_0.Queue()
    var_0 = queue_1.getTail()
    node_0 = module_0.Node(queue_0)
    var_1 = queue_0.getHead()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Queue'
    var_2 = var_1.getTail()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.Queue'
    queue_2 = module_0.Queue()
    bool_0 = var_2.isEmpty()
    assert bool_0 is False
    str_0 = var_0.__str__()
    bool_1 = queue_1.isEmpty()
    assert bool_1 is True

def test_case_3():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    str_0 = doubly_linked_list_0.__str__()
    assert str_0 == '[]'
    var_0 = doubly_linked_list_0.getHead()
    var_1 = doubly_linked_list_0.removeAtTail()
    var_2 = doubly_linked_list_0.removeAtHead()
    none_type_0 = doubly_linked_list_0.addAtHead(var_2)
    assert len(doubly_linked_list_0) == 1
    var_3 = doubly_linked_list_0.getHead()

def test_case_4():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.isEmpty()
    assert bool_0 is True
    var_0 = queue_0.dequeue()

def test_case_5():
    none_type_0 = None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    queue_0 = module_0.Queue()
    int_0 = queue_0.getSize()
    assert int_0 == 0
    node_0 = module_0.Node(none_type_0)
    int_1 = doubly_linked_list_0.getSize()
    assert int_1 == 0
    queue_1 = module_0.Queue()
    var_0 = queue_1.getHead()

def test_case_6():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()

def test_case_7():
    bool_0 = False
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    none_type_0 = queue_0.enqueue(bool_0)
    str_1 = queue_0.__str__()
    assert str_1 == '[False]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_1 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_0 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 0
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = doubly_linked_list_0.getTail()
    assert len(var_1) == 0
    var_2 = doubly_linked_list_0.getTail()
    assert len(var_2) == 0
    var_3 = doubly_linked_list_0.removeAtTail()
    bool_1 = var_1.isEmpty()
    assert bool_1 is True
    queue_1 = module_0.Queue()
    var_4 = queue_1.getHead()
    var_5 = queue_1.getHead()
    var_6 = doubly_linked_list_0.getTail()
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_6) == 0
    none_type_2 = doubly_linked_list_0.addAtTail(var_6)
    assert len(var_0.value) == 1
    assert len(var_6) == 1
    var_7 = var_6.getHead()
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_7) == 1

def test_case_8():
    bool_0 = True
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    none_type_0 = queue_0.enqueue(bool_0)
    str_0 = queue_0.__str__()
    assert str_0 == '[True]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    none_type_1 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.getTail()
    assert len(var_1) == 1
    var_2 = doubly_linked_list_0.getTail()
    assert len(var_2) == 1
    var_3 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert len(var_1) == 0
    assert len(var_2) == 0
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue3.Node'
    assert f'{type(var_3.value).__module__}.{type(var_3.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_3.value) == 0
    assert var_3.next is None
    assert var_3.prev is None
    bool_1 = var_1.isEmpty()
    assert bool_1 is True
    bool_2 = var_1.isEmpty()
    assert bool_2 is True
    queue_1 = module_0.Queue()
    var_4 = queue_1.getHead()
    var_5 = queue_1.getHead()
    var_6 = doubly_linked_list_0.getTail()
    none_type_2 = doubly_linked_list_0.addAtTail(var_6)
    assert len(doubly_linked_list_0) == 1
    assert len(var_1) == 1
    assert len(var_2) == 1
    assert len(var_3.value) == 1

def test_case_9():
    bool_0 = True
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    none_type_0 = queue_0.enqueue(bool_0)
    str_0 = queue_0.__str__()
    assert str_0 == '[True]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    none_type_1 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_1.value) == 0
    assert var_1.next is None
    assert var_1.prev is None
    var_2 = doubly_linked_list_0.getTail()
    var_3 = doubly_linked_list_0.getTail()
    var_4 = doubly_linked_list_0.removeAtTail()

def test_case_10():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    none_type_0 = doubly_linked_list_1.addAtTail(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    none_type_1 = None
    str_0 = doubly_linked_list_1.__str__()
    none_type_2 = doubly_linked_list_1.addAtTail(none_type_0)
    assert len(doubly_linked_list_1) == 2
    str_1 = doubly_linked_list_1.__str__()
    var_0 = doubly_linked_list_1.getTail()
    var_1 = doubly_linked_list_1.removeAtTail()
    assert len(doubly_linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert var_1.value is None
    assert var_1.next is None
    assert var_1.prev is None
    none_type_3 = doubly_linked_list_1.addAtHead(str_0)
    assert len(doubly_linked_list_1) == 2
    var_2 = doubly_linked_list_1.getTail()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_2) == 2
    none_type_4 = doubly_linked_list_1.addAtHead(var_2)
    assert len(doubly_linked_list_1) == 3
    assert len(var_2) == 3
    none_type_5 = doubly_linked_list_1.addAtTail(none_type_1)
    assert len(doubly_linked_list_1) == 4
    assert len(var_2) == 4
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
