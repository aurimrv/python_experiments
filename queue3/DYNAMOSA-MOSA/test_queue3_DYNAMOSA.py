#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue3/DYNAMOSA/test_queue3.py.orig
import pytest
import queue3 as module_0

def test_case_0():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0

def test_case_1():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    str_0 = doubly_linked_list_0.__str__()
    assert str_0 == '[]'
    none_type_0 = doubly_linked_list_0.addAtHead(str_0)
    assert len(doubly_linked_list_0) == 1
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 1
    var_0 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert var_0.value == '[]'
    assert var_0.next is None
    assert var_0.prev is None
    str_1 = doubly_linked_list_0.__str__()
    assert str_1 == '[]'
    queue_0 = module_0.Queue()
    var_1 = queue_0.getTail()

def test_case_2():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.getHead()
    none_type_0 = doubly_linked_list_0.addAtTail(var_0)
    assert len(doubly_linked_list_0) == 1

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_4():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.removeAtTail()

def test_case_5():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()
    str_0 = var_0.__str__()
    bool_0 = queue_0.isEmpty()
    assert bool_0 is True

def test_case_6():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.getHead()
    var_1 = doubly_linked_list_0.getHead()

def test_case_7():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getTail()

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

def test_case_11():
    int_0 = 286
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(int_0)
    bool_0 = queue_0.isEmpty()
    assert bool_0 is False
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert var_0.value == 286
    assert var_0.next is None
    assert var_0.prev is None

def test_case_12():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()
    int_0 = queue_0.getSize()

def test_case_13():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    str_0 = doubly_linked_list_0.__str__()
    assert str_0 == '[]'
    none_type_0 = doubly_linked_list_0.addAtHead(str_0)
    assert len(doubly_linked_list_0) == 1
    int_0 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(int_0).__module__}.{type(int_0).__qualname__}' == 'queue3.Node'
    assert int_0.value == '[]'
    assert int_0.next is None
    assert int_0.prev is None
    var_0 = doubly_linked_list_0.removeAtHead()
    str_1 = doubly_linked_list_0.__str__()
    queue_0 = module_0.Queue()
    var_1 = queue_0.getTail()

def test_case_14():
    int_0 = 286
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    queue_1 = module_0.Queue()
    none_type_0 = queue_1.enqueue(int_0)
    bool_0 = queue_1.isEmpty()
    assert bool_0 is False
    var_0 = module_0.DoublyLinkedList()
    assert len(var_0) == 0
    str_1 = queue_1.__str__()
    assert str_1 == '[286]'
    none_type_1 = queue_1.enqueue(none_type_0)
    var_1 = var_0.getTail()
    var_2 = queue_1.getTail()

def test_case_15():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_0 = doubly_linked_list_0.getHead()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0) == 1
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    int_0 = doubly_linked_list_1.getSize()
    assert int_0 == 0
    str_1 = doubly_linked_list_1.__str__()
    var_1 = doubly_linked_list_1.removeAtTail()

def test_case_16():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()
    none_type_1 = doubly_linked_list_0.addAtHead(str_0)
    assert len(doubly_linked_list_0) == 2
    var_0 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 1
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 0
    assert len(var_0.value) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert var_1.next is None
    assert var_1.prev is None
    str_1 = doubly_linked_list_0.__str__()
    assert str_1 == '[]'
    queue_0 = module_0.Queue()
    var_2 = queue_0.getTail()

def test_case_17():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    none_type_1 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    str_0 = doubly_linked_list_0.__str__()
    none_type_2 = doubly_linked_list_0.addAtHead(str_0)
    assert len(doubly_linked_list_0) == 3
    var_0 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 2
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 2
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = doubly_linked_list_0.removeAtHead()
    assert len(doubly_linked_list_0) == 1
    assert len(var_0.value) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue3.Node'
    assert var_1.next is None
    assert var_1.prev is None
    str_1 = doubly_linked_list_0.__str__()
    queue_0 = module_0.Queue()
    var_2 = queue_0.getTail()
    var_3 = queue_0.getTail()