#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/queue2/MOSA/test_queue2.py
import pytest
import queue2 as module_0

def test_case_0():
    int_0 = 337
    linked_node_0 = module_0.LinkedNode(int_0)
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 3
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[None,None,None]'

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0

def test_case_3():
    str_0 = ' \x0c0oS}j^g'
    linked_node_0 = module_0.LinkedNode(str_0)
    linked_node_1 = module_0.LinkedNode(str_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False
    var_1 = module_0.LinkedList()
    assert len(var_1) == 0
    with pytest.raises(Exception):
        var_1.pop()

def test_case_4():
    str_0 = ' \x0c0oS j=g'
    linked_node_0 = module_0.LinkedNode(str_0)
    linked_node_1 = module_0.LinkedNode(str_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False
    linked_node_2 = module_0.LinkedNode(var_0)
    assert linked_node_2.value is False
    list_0 = []
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 0
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0
    var_2 = queue_linked_list_1.append(list_0)
    assert len(queue_linked_list_1) == 1
    linked_list_1 = module_0.LinkedList(*queue_linked_list_1)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_3 = linked_list_0.__len__()
    assert var_3 == 0
    var_4 = queue_linked_list_1.append(queue_linked_list_1)
    assert len(queue_linked_list_1) == 2
    var_5 = var_4.__repr__()
    var_6 = linked_list_1.pop()
    assert len(linked_list_1) == 0
    var_7 = queue_linked_list_0.__iter__()

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    var_2 = linked_list_1.remove(queue_linked_list_0)
    assert var_2 is False
    var_3 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 1
    var_4 = linked_node_0.checkInfinite()
    assert var_4 is False
    var_5 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert len(linked_node_0.value) == 0
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_5) == 0

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = linked_list_0.__repr__()
    assert var_1 == 'link:[]'
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_7():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = var_0.__repr__()
    assert var_1 == '0'
    var_2 = var_1.__repr__()
    assert var_2 == "'0'"
    var_3 = var_2.__len__()
    var_4 = var_3.__repr__()
    int_0 = 325
    list_0 = [int_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 1
    var_5 = linked_list_0.__len__()
    assert var_5 == 1

def test_case_8():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__iter__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    var_1 = linked_list_0.__len__()
    assert var_1 == 0

def test_case_9():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]

def test_case_10():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_11():
    list_0 = []
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(list_0)
    assert len(queue_linked_list_0) == 1
    linked_list_0 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0

def test_case_12():
    bytes_0 = b':\xf2&\x11\xdfY\xb5\xf0\xe0\xb5\xd4\xfe\xf9'
    dict_0 = {bytes_0: bytes_0}
    linked_node_0 = module_0.LinkedNode(dict_0)
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_1) == 0

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_14():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__repr__()
    assert var_0 == 'queue:[]'

def test_case_15():
    str_0 = ' \x0c0oS j=g'
    linked_node_0 = module_0.LinkedNode(str_0)
    linked_node_1 = module_0.LinkedNode(str_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False
    list_0 = []
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 0
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    queue_linked_list_1 = module_0.QueueLinkedList()
    assert len(queue_linked_list_1) == 0
    var_2 = queue_linked_list_1.append(list_0)
    assert len(queue_linked_list_1) == 1
    linked_list_1 = module_0.LinkedList(*queue_linked_list_1)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_3 = linked_list_0.__len__()
    assert var_3 == 0
    var_4 = queue_linked_list_1.__repr__()
    assert var_4 == 'queue:[[]]'
    var_5 = queue_linked_list_0.isEmpty()
    assert var_5 is True
    queue_linked_list_2 = module_0.QueueLinkedList()
    assert len(queue_linked_list_2) == 0

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 0

def test_case_17():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.isEmpty()
    assert var_0 is True
    var_1 = var_0.__repr__()
    assert var_1 == 'True'

def test_case_18():
    list_0 = []
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.append(list_0)
    assert len(queue_linked_list_0) == 1
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_2 = linked_list_1.remove(queue_linked_list_0)
    assert var_2 is False
    var_3 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 2
    var_4 = var_3.__repr__()
    var_5 = linked_node_0.checkInfinite()
    assert var_5 is False
    var_6 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 1
    assert len(linked_node_0.value) == 1

def test_case_19():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)

def test_case_20():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 2
    linked_node_1 = module_0.LinkedNode(var_1)
    var_2 = linked_node_0.checkInfinite()
    assert var_2 is False
    var_3 = queue_linked_list_0.__len__()
    assert var_3 == 2
    var_4 = linked_node_1.checkInfinite()
    linked_node_2 = module_0.LinkedNode(var_1, var_2)

def test_case_21():
    list_0 = []
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_2 = queue_linked_list_0.append(list_0)
    assert len(queue_linked_list_0) == 1
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_3 = linked_list_1.remove(queue_linked_list_0)
    assert var_3 is False
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 1
    var_4 = linked_node_0.checkInfinite()
    assert var_4 is False
    var_5 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert len(linked_node_0.value) == 0
    var_6 = linked_list_1.__iter__()

def test_case_22():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.pop()
    assert var_0 is False
    assert len(linked_list_0) == 3
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.isEmpty()
    assert var_1 is True
    float_0 = 2535.0994
    var_2 = linked_list_0.__len__()
    assert var_2 == 3
    var_3 = queue_linked_list_0.append(var_2)
    assert len(queue_linked_list_0) == 1

def test_case_23():
    list_0 = []
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.append(list_0)
    assert len(queue_linked_list_0) == 1
    linked_list_1 = module_0.LinkedList(*queue_linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_2 = linked_list_1.remove(queue_linked_list_0)
    assert var_2 is False
    var_3 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 2
    var_4 = var_3.__repr__()

def test_case_24():
    int_0 = 708
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 3
    var_0 = linked_list_0.remove(int_0)
    assert var_0 is False
    var_1 = var_0.__repr__()
    assert var_1 == 'False'
    var_2 = var_1.__repr__()
    assert var_2 == "'False'"

def test_case_25():
    str_0 = ' \x0c0oS}j^g'
    linked_node_0 = module_0.LinkedNode(str_0)
    linked_node_1 = module_0.LinkedNode(str_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False

def test_case_26():
    str_0 = ' \x0c0oS j=g'
    none_type_0 = None
    linked_node_0 = module_0.LinkedNode(none_type_0, str_0)
    linked_node_1 = module_0.LinkedNode(str_0, linked_node_0)
