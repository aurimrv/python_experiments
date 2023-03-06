#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue4/MIO/test_queue4.py.orig
import pytest
import queue4 as module_0

def test_case_0():
    bytes_0 = b'b?v\x9f\x03\xe4\xcdN\x05j\t\xd5\x85\x8d\xe9\xcb\xea\x0fk\xc7'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'

def test_case_1():
    tuple_0 = ()
    queue_0 = module_0.Queue(tuple_0)

def test_case_2():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    queue_0 = module_0.Queue(double_linked_list_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_3():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_4():
    bytes_0 = b'b?v\x9f\x03\xe4\xcdN\x05j\t\xd5\x85\x8d\xe9\xcb\xea\x0fk\xc7'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.pop()
    assert var_0 == 199

def test_case_5():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue4.DoubleLinkedList'
    assert var_1.head is None
    assert var_1.tail is None

def test_case_6():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_7():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.append(double_linked_list_0)

def test_case_9():
    bytes_0 = b'b?v\x8e\x03\xe4\xcdN\x05j\t\x8d\xe9\xdb\xea\x0fk\xc7'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.shift()
    assert var_0 == 98

def test_case_10():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'queue4.Node'
    assert var_1.tail is None

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_12():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    double_linked_list_0 = module_0.DoubleLinkedList(queue_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.remove(queue_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_13():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)

def test_case_14():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(var_1)

def test_case_15():
    bytes_0 = b'^\x8eT\xf2\x1a\x1c\xbd&\x13\xff'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_16():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(var_0)

def test_case_17():
    bool_0 = True
    int_0 = -1990
    tuple_0 = (bool_0, bool_0, bool_0, int_0)
    double_linked_list_0 = module_0.DoubleLinkedList(tuple_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.remove(bool_0)

def test_case_18():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_19():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()

def test_case_20():
    node_0 = module_0.Node()

def test_case_21():
    node_0 = module_0.Node()
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'

def test_case_22():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_23():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.enqueue(queue_0)

def test_case_24():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
