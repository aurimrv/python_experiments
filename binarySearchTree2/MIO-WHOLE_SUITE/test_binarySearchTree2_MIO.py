#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree2/MIO/test_binarySearchTree2.py.orig
import pytest
import binarySearchTree2 as module_0

def test_case_0():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0

def test_case_1():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1

def test_case_2():
    dict_0 = {}
    node_0 = module_0.Node(dict_0)
    int_0 = 698
    list_0 = [int_0, int_0, int_0, int_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 4
    bool_0 = True
    var_0 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 5
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_1 = b_s_t_1.remove(b_s_t_1)

def test_case_3():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.add(b_s_t_0)
    assert var_1 is False

def test_case_4():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    str_0 = 'Oz9!2~3'
    none_type_0 = b_s_t_0.build(str_0)
    assert len(b_s_t_0) == 7

def test_case_5():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1

def test_case_6():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    str_0 = 'Oz9!2~3'
    none_type_0 = b_s_t_0.build(str_0)
    assert len(b_s_t_0) == 7
    var_0 = b_s_t_0.contains(str_0)
    assert var_0 is False

def test_case_7():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.contains(b_s_t_0)
    assert var_0 is False

def test_case_8():
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

def test_case_9():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.remove(b_s_t_0)
    assert len(b_s_t_0) == 0

def test_case_10():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.remove(b_s_t_0)

def test_case_11():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    list_0 = [b_s_t_0, b_s_t_0, b_s_t_0]

def test_case_12():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(b_s_t_0)

def test_case_13():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder(b_s_t_0)

def test_case_14():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder()

def test_case_15():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.__str__()

def test_case_16():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0

def test_case_17():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.isValid()

def test_case_18():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__len__()
    assert var_0 == 0

def test_case_19():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'