#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList2/MIO/test_linkedList2.py.orig
import pytest
import linkedList2 as module_0

def test_case_0():
    str_0 = '4-?Fk.6R79JM\rhc'
    linked_node_0 = module_0.LinkedNode(str_0)
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_1():
    bool_0 = False
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)

def test_case_2():
    complex_0 = 1460.7871768642246 + 580.97j
    linked_node_0 = module_0.LinkedNode(complex_0)
    linked_node_1 = module_0.LinkedNode(linked_node_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False

def test_case_3():
    complex_0 = -87.067 - 1139.45326j
    linked_node_0 = module_0.LinkedNode(complex_0, complex_0)
    linked_node_1 = module_0.LinkedNode(complex_0, linked_node_0)

def test_case_4():
    str_0 = "B/n's!T!#w"
    linked_list_0 = module_0.LinkedList(*str_0)
    assert len(linked_list_0) == 10

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    with pytest.raises(Exception):
        linked_list_0.pop()

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.pop()
    assert len(linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(var_1) == 0

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(var_0)
    assert var_1 is False

def test_case_10():
    str_0 = 'ainlzQBW'
    linked_list_0 = module_0.LinkedList(*str_0)
    assert len(linked_list_0) == 8
    var_0 = linked_list_0.remove(linked_list_0)
    assert var_0 is False

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.remove(linked_list_0)
    assert var_0 is False

def test_case_12():
    str_0 = 'dindzQBW'
    linked_list_0 = module_0.LinkedList(*str_0)
    assert len(linked_list_0) == 8
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[W,B,Q,z,d,n,i,d]'

def test_case_13():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[None,None,None,None]'

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 0

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'

def test_case_16():
    str_0 = 'O3;O'
    bytes_0 = b'\x1e?\xbd%\xa4\x8e\x8d\xe0\x89'
    list_0 = [str_0, str_0, bytes_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 3
    var_0 = linked_list_0.__len__()
    assert var_0 == 3

def test_case_17():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.__len__()
    assert var_1 == 1

def test_case_18():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0

def test_case_19():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)

def test_case_20():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1