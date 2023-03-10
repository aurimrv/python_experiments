#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue5/WHOLE_SUITE/test_queue5.py.orig
import pytest
import queue5 as module_0

def test_case_0():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(none_type_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'

def test_case_1():
    queue_0 = module_0.Queue()
    queue_1 = module_0.Queue()
    node_0 = module_0.Node(queue_1)
    queue_2 = module_0.Queue()

def test_case_2():
    none_type_0 = None
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(none_type_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    int_0 = 3392
    tuple_0 = (int_0,)
    var_1 = queue_0.enqueue(queue_0)
    queue_1 = module_0.Queue()
    var_2 = queue_1.enqueue(tuple_0)

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_4():
    queue_0 = module_0.Queue()
    queue_1 = module_0.Queue()
    var_0 = queue_1.dequeue()
    var_1 = queue_1.enqueue(queue_1)
    assert f'{type(queue_1.head).__module__}.{type(queue_1.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_1.tail).__module__}.{type(queue_1.tail).__qualname__}' == 'queue5.Node'
    var_2 = queue_1.dequeue()
    assert queue_1.tail is None
    assert var_2.tail is None
    node_0 = module_0.Node(queue_1)

def test_case_5():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    bytes_0 = b'`\xf8e\x02J'
    var_1 = queue_0.enqueue(bytes_0)
    var_2 = queue_0.dequeue()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue5.Queue'
    assert f'{type(var_2.head).__module__}.{type(var_2.head).__qualname__}' == 'queue5.Node'
    assert f'{type(var_2.tail).__module__}.{type(var_2.tail).__qualname__}' == 'queue5.Node'
    var_3 = var_2.dequeue()
    assert var_3 == b'`\xf8e\x02J'
    assert queue_0.head is None
    assert queue_0.tail is None
    assert var_2.head is None
    assert var_2.tail is None
    var_4 = var_2.enqueue(var_1)
    var_5 = var_2.enqueue(var_2)

def test_case_6():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    var_1 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_2 = queue_0.dequeue()
    assert queue_0.tail is None
    assert var_2.tail is None

def test_case_7():
    bytes_0 = b'\x07!"'
    node_0 = module_0.Node(bytes_0)
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()
    var_1 = queue_0.dequeue()
