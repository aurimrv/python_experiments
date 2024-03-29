#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList2/WHOLE_SUITE/test_linkedList2.py.orig
import pytest
import linkedList2 as module_0
import builtins as module_1

def test_case_0():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0)
    linked_node_1 = module_0.LinkedNode(bool_0)

def test_case_1():
    tuple_0 = ()
    linked_node_0 = module_0.LinkedNode(tuple_0)
    set_0 = set()
    list_0 = []
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False
    var_1 = var_0.__repr__()
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 0
    var_2 = linked_list_0.remove(set_0)
    assert var_2 is False
    str_0 = '3'
    linked_list_1 = module_0.LinkedList(*str_0)
    assert len(linked_list_1) == 1
    var_3 = linked_list_1.prepend(linked_list_1)
    assert len(linked_list_1) == 2
    var_4 = var_2.__repr__()
    var_5 = linked_list_1.__len__()
    assert var_5 == 2
    var_6 = var_4.__iter__()
    var_7 = linked_list_1.remove(str_0)
    assert var_7 is True
    assert len(linked_list_1) == 1

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 0
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False
    object_0 = module_1.object()
    var_1 = linked_node_0.checkInfinite()
    assert var_1 is False

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0, linked_list_0)
    assert len(linked_node_0.value) == 0
    assert len(linked_node_0.next) == 0
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 0

def test_case_4():
    bool_0 = False
    bytes_0 = b'\x14\x0f\xf4'
    list_0 = [bytes_0, bytes_0, bytes_0, bool_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.__repr__()
    assert var_0 == "link:[False,b'\\x14\\x0f\\xf4',b'\\x14\\x0f\\xf4',b'\\x14\\x0f\\xf4']"
    var_1 = linked_list_0.remove(var_0)
    assert var_1 is False
    linked_list_1 = module_0.LinkedList(*bytes_0)
    assert len(linked_list_1) == 3

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    none_type_0 = None
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    linked_node_1 = module_0.LinkedNode(none_type_0)
    with pytest.raises(Exception):
        linked_list_0.pop()

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__iter__()
    var_1 = linked_list_0.__len__()
    assert var_1 == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 0

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_8():
    bool_0 = True
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(bool_0)
    assert len(linked_list_0) == 1

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.__repr__()
    assert var_0 == 'link:[]'
    var_1 = linked_list_1.prepend(linked_list_1)
    assert len(linked_list_1) == 1

def test_case_10():
    float_0 = 1448.9429
    list_0 = [float_0, float_0, float_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 3
    list_1 = []
    linked_list_1 = module_0.LinkedList(*list_1)
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.__repr__()
    assert var_0 == 'link:[]'
    var_1 = linked_list_0.pop()
    assert var_1 == pytest.approx(1448.9429, abs=0.01, rel=0.01)
    assert len(linked_list_0) == 2
    var_2 = linked_list_1.__repr__()
    assert var_2 == 'link:[]'
    var_3 = var_2.__iter__()
    var_4 = linked_list_0.remove(float_0)
    assert var_4 is True
    assert len(linked_list_0) == 1
    var_5 = linked_list_0.__iter__()
