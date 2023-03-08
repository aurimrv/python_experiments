#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack3/MIO/test_stack3.py.orig
import stack3 as module_0

def test_case_0():
    singly_linked_list_0 = module_0.SinglyLinkedList()

def test_case_1():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)

def test_case_2():
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(stack_0)
    none_type_1 = stack_0.push(stack_0)

def test_case_3():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'stack3.SinglyLinkedList'
    assert var_0.next is None

def test_case_4():
    stack_0 = module_0.Stack()
    var_0 = stack_0.pop()

def test_case_5():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is False

def test_case_7():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    list_0 = singly_linked_list_0.toArray()

def test_case_8():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()

def test_case_9():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    str_0 = singly_linked_list_0.__str__()

def test_case_10():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'

def test_case_11():
    stack_0 = module_0.Stack()
    bool_0 = stack_0.isEmpty()
    assert bool_0 is True

def test_case_12():
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(stack_0)
    bool_0 = stack_0.isEmpty()
    assert bool_0 is False

def test_case_13():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.getHead()

def test_case_14():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    node_0 = singly_linked_list_0.getHeadNode()

def test_case_15():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    int_0 = singly_linked_list_0.getSize()

def test_case_16():
    stack_0 = module_0.Stack()

def test_case_17():
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(stack_0)

def test_case_18():
    stack_0 = module_0.Stack()
    var_0 = stack_0.peek()

def test_case_19():
    stack_0 = module_0.Stack()
    int_0 = stack_0.getSize()

def test_case_20():
    stack_0 = module_0.Stack()
    str_0 = stack_0.__str__()
    assert str_0 == '[None]'