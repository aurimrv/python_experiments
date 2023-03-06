#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree2/DYNAMOSA/test_binarySearchTree2.py.orig
import pytest
import binarySearchTree2 as module_0
import builtins as module_1

def test_case_0():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0

def test_case_1():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    list_0 = [b_s_t_0]
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.__str__()
    var_2 = b_s_t_0.isValid()
    var_3 = b_s_t_0.add(b_s_t_0)
    assert var_3 is False
    var_4 = var_0.__str__()
    assert var_4 == '[]'

def test_case_2():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = var_0.__str__()
    assert var_1 == 'None'
    var_2 = b_s_t_0.getOrder(var_1)

def test_case_3():
    bytes_0 = b'\xf8h\x06\xa8\xb2\xbam\xf5Z\xc2\xe2\xfc'
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(bytes_0)
    assert len(b_s_t_0) == 12

def test_case_4():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    none_type_0 = b_s_t_0.build(var_0)
    assert len(b_s_t_0) == 2
    var_1 = b_s_t_0.add(var_0)
    assert len(b_s_t_0) == 3
    var_2 = b_s_t_0.remove(var_0)
    assert len(b_s_t_0) == 2

def test_case_5():
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

def test_case_6():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.remove(b_s_t_0)
    var_1 = var_0.__str__()
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_2 = b_s_t_0.getOrder(var_1)

def test_case_7():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    list_0 = [b_s_t_0]
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 1

def test_case_8():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    var_1 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree2.Node'
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'binarySearchTree2.BST'
    assert len(var_1.value) == 0
    assert var_1.left is None
    assert var_1.right is None

def test_case_9():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder(b_s_t_0)
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0
    var_1 = b_s_t_0.add(var_0)
    assert len(b_s_t_0) == 1
    assert len(node_0.value) == 1
    var_2 = b_s_t_0.__str__()
    assert var_2 == '[None]'
    var_3 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree2.Node'
    assert f'{type(var_3.value).__module__}.{type(var_3.value).__qualname__}' == 'binarySearchTree2.BST'
    assert len(var_3.value) == 1
    assert var_3.left is None
    assert var_3.right is None

def test_case_10():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.isValid()
    bytes_0 = b'\xf8h\x06\xa8\xb2\xbam\xf5Z\xc2\xe2\xfc'
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    none_type_0 = b_s_t_1.build(bytes_0)
    assert len(b_s_t_1) == 12

def test_case_11():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0
    none_type_0 = b_s_t_0.build(b_s_t_0)
    var_0 = module_0.Node(node_0)
    var_1 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree2.Node'
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'binarySearchTree2.BST'
    assert len(var_1.value) == 0
    assert var_1.left is None
    assert var_1.right is None
    var_2 = module_0.BST()

def test_case_12():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    var_1 = var_0.__str__()
    assert var_1 == 'None'
    var_2 = b_s_t_0.remove(b_s_t_0)
    assert len(b_s_t_0) == 0
    b_s_t_1 = module_0.BST()
    var_3 = b_s_t_0.getOrder(var_1)

def test_case_13():
    str_0 = 'preOrder'
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.getOrder(str_0)
    object_0 = module_1.object()
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0

def test_case_14():
    str_0 = 'preOrder'
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(str_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.getOrder(str_0)
    object_0 = module_1.object()
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
