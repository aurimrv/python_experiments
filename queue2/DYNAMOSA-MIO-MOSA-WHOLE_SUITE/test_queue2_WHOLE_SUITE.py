#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue2/WHOLE_SUITE/test_queue2.py.orig
import pytest
import queue2 as module_0

def test_case_0():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__repr__()
    assert var_0 == 'queue:[]'
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0
    var_1 = queue_linked_list_1.isEmpty()
    assert var_1 is True
    var_2 = queue_linked_list_1.__len__()
    assert var_2 == 0
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.__repr__()
    assert var_0 == 'link:[]'
    var_1 = var_0.__repr__()
    assert var_1 == "'link:[]'"
    var_2 = linked_list_1.__len__()
    assert var_2 == 0
    var_3 = linked_list_1.remove(var_2)
    assert var_3 is False

def test_case_2():
    bytes_0 = b''
    linked_node_0 = module_0.LinkedNode(bytes_0)
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.isEmpty()
    assert var_0 is True
    var_1 = linked_node_0.checkInfinite()
    assert var_1 is False
    var_2 = bytes_0.__repr__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0
    var_3 = queue_linked_list_1.__len__()
    assert var_3 == 0
    with pytest.raises(Exception):
        queue_linked_list_1.pop()

def test_case_3():
    int_0 = 1779

def test_case_4():
    int_0 = 317
    list_0 = [int_0, int_0, int_0, int_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.pop()
    assert var_0 == 317
    assert len(linked_list_0) == 3
    bool_0 = False
    var_1 = linked_list_0.remove(bool_0)
    assert var_1 is False
    var_2 = linked_list_0.__repr__()
    assert var_2 == 'link:[317,317,317]'
    bool_1 = True

def test_case_5():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__iter__()
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_2 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_2) == 0
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0

def test_case_6():
    bool_0 = True
    list_0 = [bool_0]
    linked_node_0 = module_0.LinkedNode(list_0)
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__repr__()
    assert var_0 == 'queue:[]'

def test_case_7():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(var_0)
    assert len(queue_linked_list_0) == 2
    var_2 = queue_linked_list_0.__len__()
    assert var_2 == 2
    var_3 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 1
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_3) == 1
    var_4 = var_3.__repr__()
    assert var_4 == 'queue:[None]'

def test_case_8():
    int_0 = -15
    list_0 = [int_0, int_0]
    linked_node_0 = module_0.LinkedNode(list_0, int_0)

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    with pytest.raises(Exception):
        linked_list_1.pop()

def test_case_10():
    int_0 = 200
    bool_0 = True
    list_0 = [int_0, bool_0, bool_0, int_0]
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.remove(int_0)
    assert var_0 is True
    assert len(linked_list_0) == 3
    var_1 = linked_list_0.prepend(list_0)
    assert len(linked_list_0) == 4
    var_2 = linked_list_0.__len__()
    assert var_2 == 4
    var_3 = linked_list_0.remove(var_0)
    assert var_3 is True
    assert len(linked_list_0) == 3
    var_4 = linked_list_0.remove(queue_linked_list_0)
    assert var_4 is False

def test_case_11():
    set_0 = set()
    str_0 = '(2|eT'
    list_0 = [str_0, set_0, str_0, str_0, str_0, str_0]

def test_case_12():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    bool_0 = False
    var_0 = queue_linked_list_0.append(bool_0)
    assert len(queue_linked_list_0) == 1
    none_type_0 = None
    var_1 = queue_linked_list_0.append(none_type_0)
    assert len(queue_linked_list_0) == 2
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_2 = queue_linked_list_0.__repr__()
    assert var_2 == 'queue:[False,None]'
    var_3 = linked_list_0.prepend(none_type_0)
    assert len(linked_list_0) == 1
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0
    var_4 = var_2.__iter__()

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = linked_list_0.__repr__()
    assert var_1 == 'link:[]'
    var_2 = queue_linked_list_0.isEmpty()
    assert var_2 is True
    var_3 = queue_linked_list_0.__len__()
    assert var_3 == 0
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    var_4 = queue_linked_list_0.isEmpty()
    assert var_4 is True
