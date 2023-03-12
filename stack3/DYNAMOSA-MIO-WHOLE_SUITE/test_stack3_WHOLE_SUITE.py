#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack3/WHOLE_SUITE/test_stack3.py.orig
import pytest
import stack3 as module_0

def test_case_0():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    node_0 = singly_linked_list_0.getHeadNode()
    singly_linked_list_1 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_1.getHead()
    var_1 = singly_linked_list_1.getHead()
    var_2 = singly_linked_list_1.remove()

def test_case_1():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    str_0 = singly_linked_list_0.__str__()
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    str_1 = singly_linked_list_0.__str__()
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'stack3.SinglyLinkedList'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'stack3.Node'
    singly_linked_list_1 = module_0.SinglyLinkedList()
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 1
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is False
    bytes_0 = b'{}\x0c\x8b"\x1d\x90\xb6\xee\xeb\xf8\xa6\xd5'

def test_case_2():
    stack_0 = module_0.Stack()
    bool_0 = stack_0.isEmpty()
    assert bool_0 is True
    var_0 = stack_0.peek()
    var_1 = stack_0.pop()

def test_case_3():
    bool_0 = False
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(bool_0)
    str_0 = stack_0.__str__()
    assert str_0 == '[False]'
    none_type_1 = stack_0.push(stack_0)
    int_0 = stack_0.getSize()
    assert int_0 == 2
    bool_1 = stack_0.isEmpty()
    assert bool_1 is False
    singly_linked_list_0 = module_0.SinglyLinkedList()
    str_1 = stack_0.__str__()
    var_0 = singly_linked_list_0.getHead()
    var_1 = singly_linked_list_0.getHead()
    var_2 = stack_0.peek()
    none_type_2 = stack_0.push(var_1)
    int_1 = stack_0.getSize()
    assert int_1 == 3
    var_3 = stack_0.peek()

def test_case_4():
    bytes_0 = b'W)\x0e\xb6\x96'
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(bytes_0)
    var_0 = stack_0.pop()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert var_0.value == b'W)\x0e\xb6\x96'
    assert var_0.next is None

def test_case_5():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 0
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'
    stack_0 = module_0.Stack()

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()

def test_case_7():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True
    bool_1 = singly_linked_list_0.isEmpty()
    assert bool_1 is True
    node_0 = singly_linked_list_0.getHeadNode()

def test_case_8():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()
    node_0 = module_0.Node(var_0)
    assert node_0.value is None
