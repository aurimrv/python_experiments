#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue3/MOSA/test_queue3.py.orig
import pytest
import queue3 as module_0

def test_case_0():
    queue_0 = module_0.Queue()

def test_case_1():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 0
    queue_0 = module_0.Queue()
    queue_1 = module_0.Queue()
    none_type_0 = queue_1.enqueue(doubly_linked_list_0)
    int_1 = queue_1.getSize()
    assert int_1 == 1
    var_0 = doubly_linked_list_0.getHead()
    none_type_1 = doubly_linked_list_0.addAtHead(var_0)
    assert len(doubly_linked_list_0) == 1

def test_case_2():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.getHead()
    none_type_0 = doubly_linked_list_0.addAtTail(var_0)
    assert len(doubly_linked_list_0) == 1

def test_case_3():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.getTail()
    var_1 = doubly_linked_list_0.removeAtHead()

def test_case_4():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.removeAtTail()

def test_case_5():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    queue_1 = module_0.Queue()
    queue_2 = module_0.Queue()
    var_1 = queue_1.dequeue()
    queue_3 = module_0.Queue()
    bool_0 = queue_0.isEmpty()
    assert bool_0 is True

def test_case_6():
    bool_0 = True
    node_0 = module_0.Node(bool_0)
    node_1 = module_0.Node(bool_0)
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()

def test_case_7():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    str_0 = doubly_linked_list_0.__str__()
    assert str_0 == '[]'
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    doubly_linked_list_1 = module_0.DoublyLinkedList()

def test_case_8():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = doubly_linked_list_0.getSize()
    assert int_0 == 0

def test_case_9():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 0

def test_case_10():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getTail()

def test_case_11():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()
    int_0 = queue_0.getSize()

def test_case_12():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.getHead()
    var_1 = doubly_linked_list_0.getHead()

def test_case_13():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    str_1 = doubly_linked_list_0.__str__()
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
    queue_0 = module_0.Queue()
    str_2 = queue_0.__str__()
    assert str_2 == '[]'
    var_0 = doubly_linked_list_1.removeAtHead()
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 1
    var_1 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_1.value) == 0
    assert var_1.next is None
    assert var_1.prev is None

def test_case_14():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    queue_0 = module_0.Queue()
    str_1 = queue_0.__str__()
    assert str_1 == '[]'
    var_0 = doubly_linked_list_1.removeAtHead()
    var_1 = queue_0.getHead()
    int_0 = doubly_linked_list_1.__len__()
    var_2 = doubly_linked_list_1.removeAtTail()

def test_case_15():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()
    queue_0 = module_0.Queue()
    str_1 = queue_0.__str__()
    assert str_1 == '[]'
    var_0 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 0
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = queue_0.getHead()

def test_case_16():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    none_type_1 = doubly_linked_list_0.addAtTail(none_type_0)
    assert len(doubly_linked_list_0) == 2
    str_0 = doubly_linked_list_0.__str__()
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    queue_0 = module_0.Queue()
    str_1 = queue_0.__str__()
    assert str_1 == '[]'
    var_0 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 1
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = queue_0.getHead()

def test_case_17():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    none_type_1 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_0 = doubly_linked_list_0.getHead()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0) == 2
    int_0 = doubly_linked_list_0.getSize()
    assert int_0 == 2
    str_0 = doubly_linked_list_0.__str__()
    var_1 = doubly_linked_list_0.getTail()
    assert len(var_1) == 2
    bool_0 = var_1.isEmpty()
    assert bool_0 is False
    var_2 = var_1.removeAtHead()
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    assert len(var_1) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.Node'
    assert f'{type(var_2.value).__module__}.{type(var_2.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_2.value) == 1
    assert var_2.next is None
    assert var_2.prev is None
    bool_1 = var_1.isEmpty()
    assert bool_1 is False
    var_3 = var_1.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert len(var_0) == 0
    assert len(var_1) == 0
    assert len(var_2.value) == 0
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue3.Node'
    assert f'{type(var_3.value).__module__}.{type(var_3.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_3.value) == 0
    assert var_3.next is None
    assert var_3.prev is None
    var_4 = doubly_linked_list_0.getTail()
    var_5 = doubly_linked_list_0.getHead()

def test_case_18():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()
    var_0 = doubly_linked_list_0.getTail()
    assert len(var_0) == 1
    var_1 = var_0.getHead()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_1) == 1
    none_type_1 = var_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    assert len(var_1) == 2
    var_2 = var_0.getHead()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_2) == 2
    var_3 = doubly_linked_list_0.getTail()
    assert len(var_3) == 2
    bool_0 = var_1.isEmpty()
    assert bool_0 is False
    var_4 = var_2.getTail()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_4) == 2

def test_case_19():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_0 = doubly_linked_list_0.getHead()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0) == 1
    int_0 = doubly_linked_list_0.getSize()
    assert int_0 == 1
    none_type_1 = var_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    str_0 = doubly_linked_list_0.__str__()
    var_1 = doubly_linked_list_0.getTail()
    assert len(var_1) == 2
    bool_0 = var_1.isEmpty()
    assert bool_0 is False
    bool_1 = var_1.isEmpty()
    assert bool_1 is False
    var_2 = var_1.removeAtTail()
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    assert len(var_1) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue3.Node'
    assert f'{type(var_2.value).__module__}.{type(var_2.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_2.value) == 1
    assert var_2.next is None
    assert var_2.prev is None
    var_3 = doubly_linked_list_0.getHead()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_3) == 1
    var_4 = var_3.getHead()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_4) == 1
    var_5 = var_4.getTail()
    assert len(var_5) == 1
    bool_2 = var_5.isEmpty()
    assert bool_2 is False