#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList4/WHOLE_SUITE/test_linkedList4.py.orig
import pytest
import linkedList4 as module_0

def test_case_0():
    str_0 = '/lG%TC'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    dict_0 = {str_0: linked_list_0}
    bytes_0 = b'O\xfb\x03'
    str_1 = 'E'
    node_0 = module_0.Node(str_1)
    var_0 = linked_list_0.push(dict_0)
    linked_list_1 = module_0.LinkedList(node_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList4.LinkedList'
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linkedList4.Node'
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None
    var_1 = linked_list_1.display()

def test_case_1():
    pass

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    int_0 = -1574
    var_1 = linked_list_0.remove(linked_list_0)
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    linked_list_2 = module_0.LinkedList(int_0)
    assert f'{type(linked_list_2.head).__module__}.{type(linked_list_2.head).__qualname__}' == 'linkedList4.Node'
    with pytest.raises(IndexError):
        linked_list_0.pop()

def test_case_3():
    bool_0 = False
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(bool_0)

def test_case_4():
    bool_0 = True
    none_type_0 = None
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.push(none_type_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    bool_1 = False
    var_1 = linked_list_0.search(bool_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList4.Node'
    assert var_1.data is True
    assert var_1.next is None
    linked_list_2 = module_0.LinkedList(bool_1)
    assert linked_list_2.head is None
    linked_list_3 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_3.head).__module__}.{type(linked_list_3.head).__qualname__}' == 'linkedList4.Node'
    var_2 = linked_list_3.pop()
    assert var_2 is True
    assert linked_list_3.head is None
    var_3 = linked_list_1.display()
    assert var_3 == ')'
    var_4 = linked_list_0.remove(var_2)
    var_5 = linked_list_3.push(linked_list_1)
    var_6 = linked_list_3.size()
    assert var_6 == 1

def test_case_5():
    str_0 = '/\t}4,ZL@'
    bytes_0 = b'\xc8\x83]\xdf\xc1t\x84\x0e\xe0\xe8\t\xf5\xf0=a'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(97, 61, 240, 245, 9, 232, 224, 14, 132, 116, 193, 223, 93, 131, 200)'
    var_1 = linked_list_0.remove(str_0)
    var_2 = linked_list_0.search(var_1)

def test_case_6():
    int_0 = 1061
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(int_0)

def test_case_7():
    int_0 = 1061
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(int_0)