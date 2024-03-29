#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree2/WHOLE_SUITE/test_binarySearchTree2.py.orig
import pytest
import binarySearchTree2 as module_0

def test_case_0():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.remove(b_s_t_0)
    assert len(b_s_t_0) == 0
    var_2 = b_s_t_0.__str__()
    assert var_2 == '[]'

def test_case_1():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.contains(b_s_t_0)
    assert var_0 is False
    var_1 = b_s_t_0.getOrder(b_s_t_0)
    var_2 = b_s_t_0.__str__()
    assert var_2 == '[]'

def test_case_2():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.isValid()

def test_case_3():
    list_0 = []
    int_0 = 1181
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(int_0)
    assert len(b_s_t_0) == 1
    var_1 = var_0.__str__()
    assert var_1 == 'None'
    tuple_0 = (list_0, int_0, var_1, var_1)
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_2 = b_s_t_1.__len__()
    assert var_2 == 0

def test_case_4():
    none_type_0 = None
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    bool_0 = False
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_0 = b_s_t_1.add(bool_0)
    assert len(b_s_t_1) == 1
    var_1 = b_s_t_1.contains(bool_0)
    assert var_1 is True
    var_2 = b_s_t_1.add(var_1)
    assert len(b_s_t_1) == 2
    var_3 = var_1.__str__()
    assert var_3 == 'True'
    var_4 = b_s_t_1.remove(bool_0)
    assert len(b_s_t_1) == 1

def test_case_5():
    none_type_0 = None
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    bool_0 = False
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_0 = b_s_t_1.add(bool_0)
    assert len(b_s_t_1) == 1
    var_1 = b_s_t_1.contains(bool_0)
    assert var_1 is True
    var_2 = b_s_t_1.add(var_1)
    assert len(b_s_t_1) == 2
    var_3 = var_1.__str__()
    assert var_3 == 'True'
    var_4 = b_s_t_1.remove(bool_0)
    assert len(b_s_t_1) == 1

def test_case_6():
    bool_0 = False
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.remove(bool_0)
    assert len(b_s_t_0) == 0

def test_case_7():
    bool_0 = False
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.remove(bool_0)
    var_1 = b_s_t_0.__str__()
    assert var_1 == '[]'
    var_2 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 1
    var_3 = b_s_t_0.remove(bool_0)
    assert len(b_s_t_0) == 0

def test_case_8():
    bool_0 = False
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(bool_0)
    node_1 = module_0.Node(b_s_t_0)
    assert len(node_1.value) == 0
    var_0 = b_s_t_0.__len__()
    assert var_0 == 0
    node_2 = module_0.Node(bool_0)
    var_1 = b_s_t_0.__len__()
    assert var_1 == 0

def test_case_9():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.add(b_s_t_0)
    assert var_1 is False
    var_2 = b_s_t_0.getOrder()

def test_case_10():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0
    var_0 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree2.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'binarySearchTree2.BST'
    assert len(var_0.value) == 0
    assert var_0.left is None
    assert var_0.right is None
    node_1 = module_0.Node(node_0)
    var_1 = b_s_t_0.minValueNode(node_0)
    assert len(var_1.value) == 0

def test_case_11():
    bool_0 = True
    bytes_0 = b'`\xbb'
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder()
    none_type_0 = b_s_t_0.build(bytes_0)
    assert len(b_s_t_0) == 2
    float_0 = -4403.3
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    node_0 = module_0.Node(float_0)
    var_1 = b_s_t_1.remove(bytes_0)
    var_2 = var_1.__str__()
    var_3 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 3

def test_case_12():
    bytes_0 = b"\x13\xe3<_\xf4\x01\xb7\xbeC\xc1P\xda\x05\xc1)4'"
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder()
    none_type_0 = b_s_t_0.build(bytes_0)
    assert len(b_s_t_0) == 17
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_1 = b_s_t_1.remove(bytes_0)
    var_2 = var_1.__str__()

def test_case_13():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0

def test_case_14():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.isValid()

def test_case_15():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    str_0 = 'Uqfh9M*4'
    int_0 = 1695
    list_0 = [int_0, int_0, int_0, int_0]
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_0 = b_s_t_1.getOrder(str_0)
    var_1 = var_0.__str__()
    assert var_1 == 'None'
    var_2 = var_1.__str__()
    assert var_2 == 'None'
    b_s_t_2 = module_0.BST()
    assert len(b_s_t_2) == 0
    var_3 = b_s_t_2.add(list_0)
    assert len(b_s_t_2) == 1
    var_4 = b_s_t_2.getOrder(var_1)
