#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree1/MOSA/test_binarySearchTree1.py.orig
import pytest
import binarySearchTree1 as module_0
import builtins as module_1

def test_case_0():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    binary_node_0 = module_0.BinaryNode(var_0)
    var_1 = binary_node_0.add(var_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_node_0.remove(var_0)
    assert binary_node_0.left is None
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_2.value is False
    assert var_2.left is None
    assert var_2.right is None
    binary_node_1 = module_0.BinaryNode(binary_node_0)
    var_3 = var_2.inorder()

def test_case_1():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    bool_0 = True
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.add(bool_0)

def test_case_2():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(none_type_0)
    assert var_0 is False
    var_1 = binary_tree_0.closest(var_0)
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(var_1)
    var_2 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    object_0 = module_1.object()
    var_3 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_3.root).__module__}.{type(var_3.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_3():
    none_type_0 = None
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_0 = binary_node_0.__repr__()
    assert var_0 == '(L: None R:)'

def test_case_4():
    binary_tree_0 = module_0.BinaryTree()
    bool_0 = False
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.closest(bool_0)
    assert var_1 is False

def test_case_5():
    str_0 = 'j_XwI\'J"{^zfX[y'
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(str_0)

def test_case_6():
    binary_tree_0 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMin()

def test_case_7():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = module_0.BinaryTree()
    var_1 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMax()

def test_case_8():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = var_0.__repr__()

def test_case_9():
    float_0 = 1747.362
    dict_0 = {float_0: float_0}
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(dict_0)

def test_case_10():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__repr__()
    assert var_0 == 'binary:()'

def test_case_11():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.closest(none_type_0)
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_1 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert var_2 is True
    var_3 = binary_tree_0.remove(bool_0)
    assert binary_tree_0.root is None
    var_4 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_4.root).__module__}.{type(var_4.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = binary_tree_0.__repr__()
    assert var_5 == 'binary:(L: True R:)'
    var_6 = binary_tree_0.getMin()
    assert var_6 is True

def test_case_12():
    binary_tree_0 = module_0.BinaryTree()

def test_case_13():
    binary_tree_0 = module_0.BinaryTree()
    bool_0 = True
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = var_0.__repr__()
    var_2 = binary_tree_0.remove(bool_0)
    assert binary_tree_0.root is None
    var_3 = binary_tree_0.add(bool_0)

def test_case_14():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    binary_node_0 = module_0.BinaryNode(var_0)
    var_1 = binary_node_0.add(var_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.closest(var_0)
    var_3 = binary_node_0.remove(var_0)
    assert binary_node_0.left is None
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_3.value is False
    assert var_3.left is None
    assert var_3.right is None
    bool_0 = True
    var_4 = var_3.add(bool_0)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_3.right).__module__}.{type(var_3.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_6 = binary_tree_0.getMax()
    assert var_6 is True
    var_7 = var_3.addToSubTree(binary_tree_0, bool_0)
    var_8 = var_3.__repr__()
    assert var_8 == '(L: False R:(L: True R:))'
    object_0 = binary_node_0.removeFromParent(var_5, var_5)

def test_case_15():
    binary_tree_0 = module_0.BinaryTree()
    bool_0 = True
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.getMax()
    assert var_1 is True
    var_2 = binary_tree_0.getMin()
    assert var_2 is True
    object_0 = module_1.object()

def test_case_16():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    bool_0 = True
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.add(bool_0)
    var_3 = binary_tree_0.getMax()
    assert var_3 is True

def test_case_17():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__repr__()
    assert var_0 == 'binary:()'
    var_1 = var_0.__repr__()
    assert var_1 == "'binary:()'"
    var_2 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.getMax()
    assert var_3 == 'binary:()'
    var_4 = binary_tree_0.__iter__()
    var_5 = binary_tree_0.__contains__(var_1)
    assert var_5 is False
    bool_0 = False

def test_case_18():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.getMax()
    assert var_1 is False
    var_2 = binary_tree_0.__contains__(var_1)
    assert var_2 is True
    var_3 = binary_tree_0.closest(bool_0)
    assert var_3 is False

def test_case_19():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    object_0 = module_1.object(*binary_tree_0)

def test_case_20():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.__iter__()
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_2 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    int_0 = 427
    var_3 = binary_node_0.addToSubTree(binary_tree_0, int_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_3.root).__module__}.{type(var_3.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_4 = var_1.__repr__()
    var_5 = binary_tree_0.getMax()
    assert var_5 == 427
    var_6 = binary_tree_0.remove(var_5)

def test_case_21():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_1 = binary_tree_0.closest(none_type_0)
    bool_0 = True
    var_2 = binary_node_0.addToSubTree(none_type_0, binary_node_0)
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_2.value).__module__}.{type(var_2.value).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_2.left is None
    assert var_2.right is None
    var_3 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_4 = binary_tree_0.getMax()
    assert var_4 is True
    var_5 = binary_tree_0.remove(var_0)

def test_case_22():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.closest(var_0)
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(var_1)
    var_2 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = var_1.__repr__()
    object_0 = module_1.object()
    var_4 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_4.root).__module__}.{type(var_4.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = binary_tree_0.getMin()
    assert var_5 is True

def test_case_23():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.closest(none_type_0)
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_2 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = var_1.__repr__()
    var_4 = binary_tree_0.getMax()
    assert var_4 is True
    var_5 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_5.root).__module__}.{type(var_5.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_24():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    binary_node_0 = module_0.BinaryNode(var_0)
    var_1 = binary_node_0.add(var_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    binary_node_1 = module_0.BinaryNode(binary_node_0)
    bool_0 = True
    var_2 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(bool_0)
    var_4 = binary_node_0.__repr__()
    assert var_4 == '(L:(L: False R:) False R:)'
    var_5 = binary_tree_0.getMax()
    assert var_5 is True

def test_case_25():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.closest(none_type_0)
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_2 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = var_1.__repr__()
    var_4 = binary_tree_0.getMax()
    assert var_4 is True
    var_5 = binary_tree_0.remove(bool_0)
    assert binary_tree_0.root is None
    var_6 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_6.root).__module__}.{type(var_6.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_7 = var_4.__repr__()
    var_8 = binary_tree_0.closest(var_0)
    assert var_8 is True

def test_case_26():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.__contains__(var_0)
    var_2 = binary_tree_0.__iter__()
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(var_2)
    assert f'{type(binary_node_0.value).__module__}.{type(binary_node_0.value).__qualname__}' == 'builtins.generator'
    var_3 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    int_0 = 427
    var_4 = binary_node_0.addToSubTree(binary_tree_0, int_0)
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_4.root).__module__}.{type(var_4.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = var_2.__repr__()
    var_6 = binary_tree_0.getMax()
    assert var_6 == 427
    var_7 = binary_tree_0.remove(bool_0)
    var_8 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_8).__module__}.{type(var_8).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_8.root).__module__}.{type(var_8.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_9 = var_6.__repr__()
    assert var_9 == '427'
    var_10 = binary_tree_0.closest(var_0)
    assert var_10 is False
    object_0 = module_1.object()

def test_case_27():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    binary_node_0 = module_0.BinaryNode(var_0)
    var_1 = binary_tree_0.remove(var_0)
    var_2 = binary_tree_0.closest(var_0)
    bool_0 = True
    var_3 = binary_node_0.addToSubTree(var_2, bool_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_3.value is True
    assert var_3.left is None
    assert var_3.right is None
    var_4 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    binary_node_1 = module_0.BinaryNode(var_2)
    var_5 = binary_tree_0.add(bool_0)
    var_6 = binary_tree_0.getMax()
    assert var_6 is True
    var_7 = binary_node_1.addToSubTree(binary_tree_0, bool_0)
    var_8 = module_0.BinaryNode(binary_tree_0)
    var_9 = binary_tree_0.getMin()
    assert var_9 is True
    object_0 = module_1.object()

def test_case_28():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__iter__()
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_1 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.__repr__()
    assert var_2 == 'binary:(L: False R:)'
    int_0 = 427
    var_3 = binary_node_0.addToSubTree(binary_tree_0, int_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_3.root).__module__}.{type(var_3.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_4 = var_0.__repr__()
    var_5 = binary_tree_0.remove(bool_0)
    var_6 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_6.root).__module__}.{type(var_6.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_7 = binary_tree_0.__contains__(bool_0)
    assert var_7 is True
    var_8 = binary_tree_0.closest(int_0)
    assert var_8 == 427
    bool_1 = True
    var_9 = binary_tree_0.add(bool_1)
    var_10 = var_6.closest(bool_1)
    assert var_10 is True

def test_case_29():
    binary_tree_0 = module_0.BinaryTree()
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(binary_tree_0)
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    int_0 = 1625
    var_1 = binary_node_0.addToSubTree(binary_tree_0, int_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_1.root).__module__}.{type(var_1.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert var_2 == 1625
    var_3 = binary_tree_0.remove(bool_0)
    var_4 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_4.root).__module__}.{type(var_4.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = var_4.add(var_2)
    var_6 = binary_tree_0.__contains__(bool_0)
    assert var_6 is True
    var_7 = var_4.remove(var_2)
    var_8 = binary_tree_0.closest(var_6)
    assert var_8 is True

def test_case_30():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.__iter__()
    binary_node_0 = module_0.BinaryNode(var_0)
    var_2 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__repr__()
    assert var_3 == 'binary:(L: False R:)'
    int_0 = 427
    var_4 = binary_node_0.addToSubTree(binary_tree_0, int_0)
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_4.root).__module__}.{type(var_4.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_5 = var_1.__repr__()
    var_6 = binary_tree_0.getMax()
    assert var_6 == 427
    var_7 = binary_tree_0.__contains__(int_0)
    assert var_7 is True

def test_case_31():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    int_0 = -2656
    var_1 = binary_tree_0.add(int_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    bool_0 = False
    var_2 = var_0.__repr__()
    binary_node_0 = module_0.BinaryNode(var_0)
    var_3 = binary_tree_0.add(bool_0)
    var_4 = binary_tree_0.__repr__()
    assert var_4 == 'binary:(L: -2656 R:(L: False R:))'
    int_1 = 1625
    var_5 = binary_node_0.addToSubTree(binary_tree_0, int_1)
    var_6 = var_0.__repr__()
    var_7 = binary_tree_0.getMax()
    assert var_7 == 1625
    var_8 = binary_tree_0.remove(bool_0)
    var_9 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    var_10 = binary_tree_0.__contains__(bool_0)
    assert var_10 is True
    var_11 = var_9.remove(var_7)
    var_12 = binary_tree_0.closest(var_0)
    assert var_12 is False
    var_13 = binary_tree_0.add(var_10)

def test_case_32():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    bool_0 = True
    var_1 = var_0.__repr__()
    int_0 = 1656
    var_2 = binary_tree_0.add(int_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_0)
    var_4 = binary_tree_0.__repr__()
    assert var_4 == 'binary:(L:(L: False R:) 1656 R:)'
    binary_node_0 = module_0.BinaryNode(var_0)
    var_5 = binary_tree_0.__repr__()
    assert var_5 == 'binary:(L:(L: False R:) 1656 R:)'
    int_1 = 1625
    var_6 = binary_node_0.addToSubTree(binary_tree_0, int_1)
    var_7 = var_0.__repr__()
    var_8 = binary_tree_0.getMax()
    assert var_8 == 1656
    var_9 = binary_tree_0.remove(bool_0)
    var_10 = binary_node_0.addToSubTree(binary_tree_0, bool_0)
    var_11 = var_10.add(var_8)
    var_12 = binary_tree_0.__contains__(bool_0)
    assert var_12 is True
    var_13 = var_10.remove(var_8)
    var_14 = binary_tree_0.closest(var_0)
    assert var_14 is False