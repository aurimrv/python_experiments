#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList1/WHOLE_SUITE/test_linkedList1.py.orig
import pytest
import linkedList1 as module_0
import builtins as module_1

def test_case_0():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(StopIteration):
        doubly_linked_list_0.next()

def test_case_1():
    bool_0 = False
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(singly_linked_list_0)
    var_1 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_2 = singly_linked_list_0.__setitem__(var_0, var_0)
    var_3 = singly_linked_list_0.__getitem__(bool_0)
    assert var_3 is False

def test_case_2():
    bool_0 = False
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(var_0)
    assert len(singly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = singly_linked_list_0.__contains__(singly_linked_list_0)
    assert var_2 is True
    var_3 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    assert len(var_0) == 2
    var_4 = singly_linked_list_0.__setitem__(var_2, var_2)
    var_5 = singly_linked_list_0.__getitem__(bool_0)
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_5) == 2

def test_case_3():
    dict_0 = {}
    doubly_linked_node_0 = module_0.DoublyLinkedNode(dict_0)
    assert doubly_linked_node_0.data == {}
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(dict_0)
    assert len(doubly_linked_list_0) == 1
    with pytest.raises(StopIteration):
        doubly_linked_list_0.previous()

def test_case_4():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.__len__()
    assert var_2 == 2
    var_3 = doubly_linked_list_0.__len__()
    assert var_3 == 2
    var_4 = doubly_linked_list_1.append(var_2)
    assert len(doubly_linked_list_1) == 1
    var_5 = doubly_linked_list_1.append(var_4)
    assert len(doubly_linked_list_1) == 2
    var_6 = doubly_linked_list_1.append(var_4)
    assert len(doubly_linked_list_1) == 3
    var_7 = doubly_linked_list_1.insert(doubly_linked_list_1, var_2)
    assert len(doubly_linked_list_1) == 5
    var_8 = doubly_linked_list_1.__getitem__(var_3)
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
    var_9 = doubly_linked_list_0.__len__()
    assert var_9 == 2
    var_10 = doubly_linked_list_1.insert(doubly_linked_list_0, var_2)
    assert len(doubly_linked_list_1) == 6

def test_case_5():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.__len__()
    assert var_1 == 0
    var_2 = doubly_linked_list_1.append(var_0)
    assert len(doubly_linked_list_1) == 1
    var_3 = doubly_linked_list_1.append(var_2)
    assert len(doubly_linked_list_1) == 2
    var_4 = doubly_linked_list_1.insert(doubly_linked_list_0, var_0)
    assert len(doubly_linked_list_1) == 3

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_0 = doubly_linked_list_1.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.__len__()
    assert var_1 == 0
    var_2 = doubly_linked_list_1.append(var_1)
    assert len(doubly_linked_list_1) == 1
    singly_linked_node_0 = module_0.SinglyLinkedNode(doubly_linked_list_0)
    assert len(singly_linked_node_0.data) == 0
    var_3 = doubly_linked_list_1.insert(doubly_linked_list_0, var_0)
    assert len(doubly_linked_list_1) == 3
    with pytest.raises(StopIteration):
        doubly_linked_list_1.previous()

def test_case_7():
    int_0 = -440
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.insert(var_0, int_0)
    assert len(doubly_linked_list_0) == 3
    var_3 = doubly_linked_list_0.__len__()
    assert var_3 == 3
    var_4 = doubly_linked_list_0.__iter__()
    assert len(var_4) == 3
    var_5 = var_4.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 4
    assert len(var_4) == 4
    var_6 = var_4.append(var_5)
    assert len(doubly_linked_list_0) == 5
    assert len(var_4) == 5
    object_0 = module_1.object()
    var_7 = doubly_linked_list_0.__getitem__(var_3)
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_7) == 5
    var_8 = var_4.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 6
    assert len(var_4) == 6
    assert len(var_7) == 6
    var_9 = var_4.__contains__(var_0)
    assert var_9 is True
    singly_linked_node_0 = module_0.SinglyLinkedNode(var_3)
    assert singly_linked_node_0.data == 3

def test_case_8():
    int_0 = -440
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(int_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    var_2 = singly_linked_list_0.__len__()
    assert var_2 == 2
    var_3 = singly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = var_3.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 3
    assert len(var_3) == 3
    var_5 = var_3.append(var_4)
    assert len(singly_linked_list_0) == 4
    assert len(var_3) == 4
    object_0 = module_1.object()
    var_6 = singly_linked_list_0.__iter__()
    assert len(var_6) == 4
    var_7 = var_3.__contains__(var_2)
    assert var_7 is False

def test_case_9():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.insert(bool_0, bool_0)

def test_case_10():
    none_type_0 = None
    doubly_linked_node_0 = module_0.DoublyLinkedNode(none_type_0)
    assert doubly_linked_node_0.data is None
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1

def test_case_11():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    singly_linked_node_0 = module_0.SinglyLinkedNode(singly_linked_list_0)
    assert len(singly_linked_node_0.data) == 0

def test_case_12():
    float_0 = -212.15854
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__getitem__(float_0)

def test_case_13():
    float_0 = 307.671223
    none_type_0 = None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(float_0, none_type_0)

def test_case_14():
    float_0 = 1467.998
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__len__()
    assert var_0 == 0
    with pytest.raises(IndexError):
        singly_linked_list_0.__getitem__(float_0)

def test_case_15():
    int_0 = -615
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(int_0, int_0)

def test_case_16():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0

def test_case_17():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.next()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_1) == 1
    var_2 = singly_linked_list_0.append(var_1)
    assert len(singly_linked_list_0) == 2
    assert len(var_1) == 2

def test_case_18():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1

def test_case_19():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 1
    doubly_linked_node_0 = module_0.DoublyLinkedNode(var_1)
    assert doubly_linked_node_0.data is None
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
