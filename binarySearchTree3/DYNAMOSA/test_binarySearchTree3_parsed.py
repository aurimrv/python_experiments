#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/binarySearchTree3/DYNAMOSA/test_binarySearchTree3.py
import pytest
import binarySearchTree3 as module_0

def test_case_0():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.pre_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_1():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_2():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_3():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)

def test_case_4():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_5():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.balance()
    assert var_1 == 0
    var_2 = bst_0.breadth_first()
    queue_0 = module_0.Queue(var_2)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_3 = queue_0.dequeue()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(var_3.root).__module__}.{type(var_3.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_6():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_7():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.push(var_1)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = double_linked_list_0.append(queue_0)
    none_type_0 = None
    var_5 = queue_0.peek()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_6 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_7 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_8():
    bool_0 = True
    node_d_l_l_0 = module_0.NodeDLL(prev=bool_0)
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_9():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = queue_0.peek()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_4 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_5 = bst_0.delete(bst_0)
    assert bst_0.root is None
    var_6 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None

def test_case_10():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_11():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.peek()

def test_case_12():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0
    var_1 = bst_0.pre_order()
    var_2 = bst_0.size()
    assert var_2 == 0
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_1.root is None
    var_3 = bst_1.in_order()
    var_4 = bst_1.pre_order(bst_1)
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None

def test_case_13():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None

def test_case_14():
    bytes_0 = b';9q\xd5\xe4\\!+v\xc3\xb2\x97\xf0'
    none_type_0 = None
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.balance()
    assert var_0 == -3

def test_case_15():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_16():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_1 = bst_0.search(var_0)

def test_case_17():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0

def test_case_18():
    bytes_0 = b'\xa6"\x8b\xdam\xe3\x8fL\xeb\xcb\xeb\x95\xec'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_19():
    none_type_0 = None
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(none_type_0)

def test_case_20():
    node_d_l_l_0 = module_0.NodeDLL()

def test_case_21():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    node_d_l_l_0 = module_0.NodeDLL()
    var_0 = node_d_l_l_0.__repr__()
    assert var_0 == 'Value: None'
    var_1 = node_d_l_l_0.__repr__()
    assert var_1 == 'Value: None'

def test_case_22():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.push(var_1)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    queue_1 = module_0.Queue()

def test_case_23():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_24():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.pre_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_2 = bst_0.size()
    assert var_2 == 1

def test_case_25():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    double_linked_list_0 = module_0.DoubleLinkedList(bst_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = bst_0.search(bst_0)
    var_1 = bst_0.balance()
    assert var_1 == 0
    var_2 = bst_0.breadth_first()

def test_case_26():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.push(double_linked_list_0)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = double_linked_list_0.pop()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(var_4.head).__module__}.{type(var_4.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(var_4.tail).__module__}.{type(var_4.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_27():
    str_0 = 'LpnzcVxEf~\x0b6\x0b3IV]t'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.insert(str_0)
    var_1 = bst_0.delete(str_0)
    var_2 = bst_0.depth()
    assert var_2 == 6
    var_3 = bst_0.post_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    queue_1 = module_0.Queue(bst_0)
    assert f'{type(queue_1).__module__}.{type(queue_1).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_28():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.in_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_2 = module_0.Node(var_1)
    assert var_2.height == 1

def test_case_29():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_2 = queue_0.peek()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_3 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_4 = bst_0.delete(bst_0)
    assert bst_0.root is None
    var_5 = bst_0.contains(none_type_0)
    assert var_5 is False

def test_case_30():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.push(var_1)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = queue_0.peek()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_5 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_6 = bst_0.delete(bst_0)
    assert bst_0.root is None
    var_7 = bst_0.balance(var_2)
    assert var_7 == 0
    var_8 = double_linked_list_0.append(bst_0)
    var_9 = double_linked_list_0.shift()
    assert f'{type(var_9).__module__}.{type(var_9).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_9.root is None

def test_case_31():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(var_0)

def test_case_32():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = queue_0.peek()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_4 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_5 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_33():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.post_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_34():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.push(double_linked_list_0)
    var_3 = double_linked_list_0.push(var_2)
    var_4 = double_linked_list_0.remove(double_linked_list_0)

def test_case_35():
    str_0 = 'LpnzcVxEf~\x0b6\x0b3IV]t'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.insert(str_0)
    var_1 = bst_0.delete(str_0)
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_2 = bst_0.delete(str_0)
    queue_1 = module_0.Queue()
    var_3 = bst_0.size()
    assert var_3 == 16
    double_linked_list_0 = module_0.DoubleLinkedList(str_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_4 = var_2.__repr__()

def test_case_36():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_37():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.in_order(bst_0)
    var_2 = bst_0.balance()
    assert var_2 == 0
    var_3 = bst_0.post_order(var_1)
    var_4 = var_1.__repr__()
    var_5 = bst_0.post_order()
    queue_0 = module_0.Queue(var_5)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    queue_1 = module_0.Queue()
    assert f'{type(queue_1).__module__}.{type(queue_1).__qualname__}' == 'binarySearchTree3.Queue'
    var_6 = bst_0.size()
    assert var_6 == 1

def test_case_38():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.in_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_39():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.post_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_40():
    str_0 = 'y"rDQ['
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.insert(str_0)
    var_1 = bst_0.delete(str_0)

def test_case_41():
    str_0 = 'LpnzcVxEf~\x0b6\x0b3IV]t'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.insert(str_0)
    var_1 = bst_0.delete(str_0)
    var_2 = bst_0.depth()
    assert var_2 == 6
    var_3 = bst_0.post_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    queue_1 = module_0.Queue(var_3)
    assert f'{type(queue_1).__module__}.{type(queue_1).__qualname__}' == 'binarySearchTree3.Queue'
    var_4 = queue_0.size()
    assert var_4 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
