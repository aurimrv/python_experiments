#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList5/MOSA/test_linkedList5.py.orig
import pytest
import linkedList5 as module_0

def test_case_0():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    node_0 = module_0.Node(var_0)
    var_1 = linked_list_1.insert_to_front(node_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_1.delete(var_1)
    var_3 = linked_list_1.__len__()
    assert var_3 == 1
    var_4 = node_0.__str__()
    node_1 = module_0.Node(var_1, var_3)
    assert node_1.next == 1
    assert f'{type(node_1.data).__module__}.{type(node_1.data).__qualname__}' == 'linkedList5.Node'

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.delete_alt(var_0)
    var_3 = linked_list_1.print_list()
    var_4 = linked_list_0.print_list()
    var_5 = linked_list_0.__len__()
    assert var_5 == 0
    linked_list_2 = module_0.LinkedList(var_5)
    assert linked_list_2.head == 0
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_6 = linked_list_1.find(var_4)

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 0
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.delete(dict_0)
    node_0 = module_0.Node(var_0, var_0)
    var_3 = linked_list_0.__len__()
    assert var_3 == 0
    node_1 = module_0.Node(linked_list_0)
    assert len(node_1.data) == 0
    var_4 = linked_list_0.__len__()
    assert var_4 == 0
    var_5 = var_2.__str__()

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.print_list()
    var_1 = linked_list_0.find(linked_list_0)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_2 = linked_list_0.get_all_data()
    var_3 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_3.data) == 1
    linked_list_2 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_2.head) == 1
    var_4 = linked_list_2.insert_to_front(var_0)

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    var_1 = var_0.__str__()
    var_2 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_2.data) == 1
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 1

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.delete(linked_list_1)
    var_3 = linked_list_0.__len__()
    assert var_3 == 1
    linked_list_2 = module_0.LinkedList(var_3)
    assert linked_list_2.head == 1
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_4 = linked_list_1.find(var_2)
    node_1 = module_0.Node(linked_list_2, linked_list_0)
    assert len(node_1.next) == 1

def test_case_6():
    str_0 = '8'
    bool_0 = False
    linked_list_0 = module_0.LinkedList(bool_0)

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 1
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = var_1.__str__()
    var_4 = linked_list_0.delete(var_3)
    var_5 = linked_list_0.__len__()
    assert var_5 == 1
    linked_list_2 = module_0.LinkedList(var_5)
    assert linked_list_2.head == 1
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_6 = linked_list_1.find(var_4)
    var_7 = linked_list_1.append(var_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'linkedList5.Node'
    node_1 = module_0.Node(linked_list_2, var_3)
    assert node_1.next == []

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = linked_list_0.delete_alt(linked_list_0)
    linked_list_2 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_2.head) == 0
    var_0 = linked_list_2.append(linked_list_1)
    node_0 = module_0.Node(linked_list_1, linked_list_1)
    var_1 = linked_list_0.__len__()
    assert var_1 == 0
    linked_list_3 = module_0.LinkedList(var_1)
    assert linked_list_3.head == 0
    node_1 = module_0.Node(linked_list_1)
    var_2 = linked_list_0.__len__()
    assert var_2 == 0
    var_3 = var_0.__str__()

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_1.delete_alt(linked_list_1)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    var_3 = linked_list_1.print_list()
    var_4 = linked_list_0.delete(dict_0)
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_5 = linked_list_1.find(var_4)

def test_case_10():
    bool_0 = True
    bool_1 = True
    set_0 = {bool_1, bool_1, bool_1}
    linked_list_0 = module_0.LinkedList(set_0)

def test_case_11():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(none_type_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.delete_alt(linked_list_0)
    var_2 = var_1.__str__()
    var_3 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_3.data) == 2
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 2

def test_case_13():
    none_type_0 = None
    none_type_1 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(none_type_1)

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_16():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    var_0 = node_0.__str__()
    var_1 = node_0.__str__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_17():
    bool_0 = False
    linked_list_0 = module_0.LinkedList(bool_0)

def test_case_18():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete_alt(var_0)
    var_4 = linked_list_0.delete(var_3)
    var_5 = linked_list_0.__len__()
    assert var_5 == 2
    linked_list_2 = module_0.LinkedList(var_5)
    assert linked_list_2.head == 2
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_6 = linked_list_1.find(var_4)
    var_7 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_7.data) == 2
    node_1 = module_0.Node(linked_list_2, var_3)

def test_case_19():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 0
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.delete(dict_0)
    var_3 = linked_list_0.__len__()
    assert var_3 == 0
    var_4 = linked_list_0.insert_to_front(dict_0)
    assert len(linked_list_0) == 1
    assert len(linked_list_1.head) == 1
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.Node'
    assert var_4.next is None
    assert f'{type(var_4.data).__module__}.{type(var_4.data).__qualname__}' == 'builtins.dict'
    assert len(var_4.data) == 1
    var_5 = linked_list_0.get_all_data()
    linked_list_2 = module_0.LinkedList(var_3)
    assert linked_list_2.head == 0
    node_0 = module_0.Node(var_3)
    assert node_0.data == 0
    var_6 = var_2.__str__()

def test_case_20():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 1
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete_alt(var_0)
    var_4 = linked_list_1.delete(var_0)
    assert len(linked_list_1) == 0

def test_case_21():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = module_0.Node(linked_list_0, linked_list_0)
    assert len(var_0.next) == 0
    assert len(var_0.data) == 0
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 1
    assert len(var_0.next) == 1
    assert len(var_0.data) == 1
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete_alt(var_0)
    var_4 = linked_list_0.__len__()
    assert var_4 == 1
    linked_list_2 = module_0.LinkedList(var_4)
    assert linked_list_2.head == 1
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_5 = linked_list_1.find(var_0)
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'linkedList5.Node'
    var_6 = linked_list_1.append(linked_list_2)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_5.next).__module__}.{type(var_5.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'linkedList5.Node'
    assert var_6.next is None
    assert f'{type(var_6.data).__module__}.{type(var_6.data).__qualname__}' == 'linkedList5.LinkedList'
    node_1 = module_0.Node(linked_list_2, var_3)

def test_case_22():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_0.insert_to_front(linked_list_1)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 0
    var_2 = linked_list_0.delete_alt(var_0)
    var_3 = linked_list_0.delete(var_2)
    var_4 = linked_list_0.__len__()
    assert var_4 == 1
    var_5 = var_3.__str__()
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 0
    var_6 = linked_list_1.find(var_3)
    var_7 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 1
    assert len(var_1.data) == 1
    assert len(node_0.data) == 1
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_7.data) == 1
    var_8 = linked_list_0.find(linked_list_0)

def test_case_23():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.delete_alt(linked_list_0)
    assert len(linked_list_0) == 1
    assert len(var_0.data) == 1
    assert var_1.next is None
    var_3 = var_2.__str__()
    var_4 = linked_list_0.delete(var_2)
    var_5 = linked_list_0.__len__()
    assert var_5 == 1
    linked_list_1 = module_0.LinkedList(var_5)
    assert linked_list_1.head == 1

def test_case_24():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.insert_to_front(linked_list_1)
    assert len(linked_list_1) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.delete_alt(linked_list_0)
    var_3 = linked_list_0.delete(var_2)
    var_4 = linked_list_0.__len__()
    assert var_4 == 1
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_5 = linked_list_1.find(var_3)
    var_6 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(node_0.data) == 2
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'linkedList5.Node'
    assert var_6.next is None
    assert f'{type(var_6.data).__module__}.{type(var_6.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_6.data) == 2
    node_1 = module_0.Node(linked_list_1, var_4)
    assert node_1.next == 1
    assert len(node_1.data) == 2
    var_7 = linked_list_1.delete(linked_list_0)
    var_8 = linked_list_1.delete_alt(var_4)
    var_9 = linked_list_1.append(var_6)
    assert len(linked_list_1) == 3
    assert len(var_0.data) == 3
    assert len(node_0.data) == 3
    assert f'{type(var_6.next).__module__}.{type(var_6.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_6.data) == 3
    assert len(node_1.data) == 3
    assert f'{type(var_9.data).__module__}.{type(var_9.data).__qualname__}' == 'linkedList5.Node'

def test_case_25():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.delete_alt(var_0)
    var_3 = linked_list_0.delete(var_2)
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_4 = linked_list_1.find(var_3)
    var_5 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_5.data) == 2
    var_6 = node_0.__str__()
    assert len(var_6) == 2
    var_7 = var_6.print_list()
    var_8 = linked_list_1.delete(linked_list_0)
    var_9 = linked_list_1.delete_alt(var_0)

def test_case_26():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert var_2.data == []
    var_3 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 2
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.Node'
    var_4 = linked_list_0.delete(var_3)
    var_5 = linked_list_0.__len__()
    assert var_5 == 2
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_6 = linked_list_1.find(var_4)
    var_7 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_7.data) == 2
    var_8 = linked_list_0.find(linked_list_1)

def test_case_27():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
    var_2 = linked_list_0.__len__()
    assert var_2 == 1
    var_3 = linked_list_0.append(var_2)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(var_1) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert var_3.data == 1
    var_4 = linked_list_0.get_all_data()
    var_5 = linked_list_0.find(var_4)
    var_6 = var_1.delete_alt(var_1)
    var_7 = linked_list_0.delete_alt(var_4)
    var_8 = var_1.print_list()
    var_9 = linked_list_0.delete(var_4)
    var_10 = linked_list_0.__len__()
    assert var_10 == 2

def test_case_28():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.insert_to_front(var_1)
    assert len(linked_list_0) == 1
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete_alt(var_0)
    var_4 = linked_list_0.delete(var_3)
    var_5 = linked_list_0.__len__()
    assert var_5 == 1
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 1
    var_6 = linked_list_1.find(var_4)
    var_7 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(node_0.data) == 2
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_7.data) == 2
    var_8 = node_0.__str__()
    assert len(var_8) == 2
    var_9 = linked_list_1.insert_to_front(var_0)
    assert len(linked_list_1) == 3
    assert len(node_0.data) == 3
    assert len(var_7.data) == 3
    assert len(var_8) == 3
    assert f'{type(var_9).__module__}.{type(var_9).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_9.next).__module__}.{type(var_9.next).__qualname__}' == 'linkedList5.Node'
    assert var_9.data == []
    node_1 = module_0.Node(linked_list_1, var_5)
    assert node_1.next == 1
    assert len(node_1.data) == 3
    var_10 = linked_list_1.delete(linked_list_0)

def test_case_29():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
    var_2 = linked_list_0.__len__()
    assert var_2 == 1
    var_3 = linked_list_0.append(var_2)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(var_1) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert var_3.data == 1
    var_4 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.insert_to_front(var_4)
    assert len(linked_list_1) == 1
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'builtins.list'
    assert len(var_5.data) == 2
    var_6 = linked_list_0.append(var_2)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert len(var_1) == 3
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'linkedList5.Node'
    assert var_6.next is None
    assert var_6.data == 1
    var_7 = linked_list_0.find(var_4)
    var_8 = linked_list_1.delete_alt(linked_list_1)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0, var_8: linked_list_0}
    var_9 = linked_list_0.delete_alt(var_4)
    var_10 = linked_list_1.print_list()
    var_11 = linked_list_0.delete(dict_0)
    var_12 = linked_list_0.__len__()
    assert var_12 == 3

def test_case_30():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
    var_2 = linked_list_0.__len__()
    assert var_2 == 1
    var_3 = linked_list_0.append(var_2)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(var_1) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert var_3.data == 1
    var_4 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.insert_to_front(var_4)
    assert len(linked_list_1) == 1
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'builtins.list'
    assert len(var_5.data) == 2
    var_6 = linked_list_0.find(var_4)
    var_7 = linked_list_1.delete_alt(linked_list_1)
    var_8 = linked_list_0.delete_alt(var_4)
    var_9 = linked_list_1.print_list()
    var_10 = var_1.delete(var_2)
    assert len(linked_list_0) == 1
    assert var_0.next is None
    assert len(var_0.data) == 1
    assert len(var_1) == 1

def test_case_31():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
    float_0 = -317.38661
    var_2 = linked_list_0.append(float_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(var_1) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert var_2.data == pytest.approx(-317.38661, abs=0.01, rel=0.01)
    var_3 = linked_list_0.__len__()
    assert var_3 == 2
    var_4 = linked_list_0.append(var_3)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert len(var_1) == 3
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.Node'
    assert var_4.next is None
    assert var_4.data == 2
    var_5 = linked_list_0.get_all_data()
    var_6 = linked_list_0.print_list()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_7 = linked_list_1.insert_to_front(var_5)
    assert len(linked_list_1) == 1
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert var_7.next is None
    assert f'{type(var_7.data).__module__}.{type(var_7.data).__qualname__}' == 'builtins.list'
    assert len(var_7.data) == 3
    var_8 = linked_list_0.append(var_3)
    assert len(linked_list_0) == 4
    assert len(var_0.data) == 4
    assert len(var_1) == 4
    assert f'{type(var_4.next).__module__}.{type(var_4.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_8).__module__}.{type(var_8).__qualname__}' == 'linkedList5.Node'
    assert var_8.next is None
    assert var_8.data == 2
