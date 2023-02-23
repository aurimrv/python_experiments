#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/binarySearchTree1/MIO/test_binarySearchTree1.py
import pytest
import binarySearchTree1 as module_0
import builtins as module_1

def test_case_0():
    bool_0 = True
    bool_1 = False
    binary_node_0 = module_0.BinaryNode(bool_1)
    var_0 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_1():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.addToSubTree(binary_node_0, bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_2():
    bool_0 = True
    bool_1 = False
    binary_node_0 = module_0.BinaryNode(bool_1)
    var_0 = binary_node_0.remove(bool_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_0.value is False
    assert var_0.left is None
    assert var_0.right is None

def test_case_3():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.removeFromParent(binary_node_0, bool_0)

def test_case_4():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.addToSubTree(binary_node_0, bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = var_0.removeFromParent(binary_node_0, bool_0)
    assert binary_node_0.left is None
    assert var_0.left is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_1.value is True
    assert var_1.left is None
    assert var_1.right is None

def test_case_5():
    str_0 = 'X>'
    str_1 = 'qkr(Szzyf\t'
    binary_node_0 = module_0.BinaryNode(str_1)
    var_0 = binary_node_0.remove(str_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_0.value == 'qkr(Szzyf\t'
    assert var_0.left is None
    assert var_0.right is None
    binary_node_1 = module_0.BinaryNode(var_0)
    assert f'{type(binary_node_1.value).__module__}.{type(binary_node_1.value).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_6():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.removeFromParent(bool_0, bool_0)

def test_case_7():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.addToSubTree(binary_node_0, bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_node_0.removeFromParent(binary_node_0, bool_0)
    assert binary_node_0.left is None
    assert var_0.left is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_1.value is False
    assert var_1.left is None
    assert var_1.right is None
    bool_1 = True
    binary_tree_0 = module_0.BinaryTree()
    var_2 = var_0.addToSubTree(var_0, bool_1)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_1.right).__module__}.{type(var_1.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_2.value is False
    assert var_2.left is None
    assert f'{type(var_2.right).__module__}.{type(var_2.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = var_0.__repr__()
    assert var_3 == '(L: False R:(L: True R:))'
    var_4 = var_3.__repr__()
    assert var_4 == "'(L: False R:(L: True R:))'"

def test_case_8():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.__repr__()
    assert var_0 == '(L: False R:)'

def test_case_9():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.addToSubTree(binary_node_0, bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = var_0.__repr__()
    assert var_1 == '(L:(L: True R:) True R:)'

def test_case_10():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_11():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_12():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_13():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_14():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)

def test_case_15():
    binary_tree_0 = module_0.BinaryTree()
    binary_tree_1 = module_0.BinaryTree()
    var_0 = binary_tree_0.__repr__()
    assert var_0 == 'binary:()'
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.add(var_0)
    var_3 = binary_tree_0.__iter__()
    var_4 = var_3.__repr__()
    var_5 = binary_tree_0.getMin()
    assert var_5 == 'binary:()'

def test_case_16():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.getMin()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_1.root).__module__}.{type(var_1.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_17():
    binary_tree_0 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMin()

def test_case_18():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.getMax()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_1.root).__module__}.{type(var_1.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_19():
    binary_tree_0 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMax()

def test_case_20():
    binary_tree_0 = module_0.BinaryTree()
    set_0 = {binary_tree_0}
    var_0 = binary_tree_0.add(set_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.__contains__(set_0)
    assert var_1 is True

def test_case_21():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_22():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False

def test_case_23():
    bool_0 = True
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.closest(bool_0)
    assert var_1 is True

def test_case_24():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)

def test_case_25():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_26():
    binary_tree_0 = module_0.BinaryTree()
    object_0 = module_1.object(*binary_tree_0)

def test_case_27():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__repr__()
    assert var_0 == 'binary:()'

def test_case_28():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_29():
    binary_tree_0 = module_0.BinaryTree()

def test_case_30():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)
