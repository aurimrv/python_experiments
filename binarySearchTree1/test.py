#Pyguin test cases subset from ../../binarySearchTree1/RANDOM/test_binarySearchTree1_RANDOM.py
import pytest
import binarySearchTree1 as module_0
import builtins as module_1

def test_case_1017():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__repr__()
    assert var_0 == 'binary:()'
    binary_node_0 = module_0.BinaryNode(var_0)
    assert binary_node_0.value == 'binary:()'
    none_type_0 = None
    binary_tree_1 = module_0.BinaryTree()
    var_1 = binary_tree_1.add(none_type_0)
    assert f'{type(binary_tree_1.root).__module__}.{type(binary_tree_1.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = var_1.__repr__()
    binary_tree_2 = module_0.BinaryTree()
    var_3 = binary_tree_2.__iter__()
    binary_node_1 = module_0.BinaryNode(var_3)
    assert f'{type(binary_node_1.value).__module__}.{type(binary_node_1.value).__qualname__}' == 'builtins.generator'
    binary_tree_3 = module_0.BinaryTree()
    var_4 = binary_tree_3.__iter__()
    var_5 = binary_tree_3.closest(var_4)
    var_6 = var_3.__iter__()
    var_7 = var_4.__repr__()
    none_type_1 = None
    binary_tree_4 = module_0.BinaryTree()
    var_8 = binary_tree_4.add(none_type_1)
    binary_tree_5 = module_0.BinaryTree()
    binary_node_2 = module_0.BinaryNode(none_type_1)
    var_9 = binary_tree_2.__contains__(binary_tree_0)
    assert var_9 is False

def test_case_1071():
    none_type_0 = None
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(none_type_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    none_type_1 = None
    binary_tree_1 = module_0.BinaryTree()
    var_1 = binary_tree_1.add(none_type_1)
    none_type_2 = None
    binary_tree_2 = module_0.BinaryTree()
    var_2 = binary_tree_2.add(none_type_2)
    binary_node_0 = module_0.BinaryNode(binary_tree_2)
    binary_tree_3 = module_0.BinaryTree()
    binary_tree_4 = module_0.BinaryTree()
    var_3 = binary_tree_4.__iter__()
    binary_tree_5 = module_0.BinaryTree()
    var_4 = var_3.__iter__()
