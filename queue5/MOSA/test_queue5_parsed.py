#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/queue5/MOSA/test_queue5.py
import pytest
import queue5 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'

def test_case_1():
    queue_0 = module_0.Queue()
    bool_0 = True
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    queue_1 = module_0.Queue()
    queue_2 = module_0.Queue()
    node_0 = module_0.Node(bool_0)
    var_1 = queue_2.dequeue()
    var_2 = queue_0.enqueue(bool_0)

def test_case_2():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.dequeue()
    assert queue_0.head is None
    assert queue_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue5.Queue'
    assert var_1.head is None
    assert var_1.tail is None

def test_case_4():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.enqueue(queue_0)
    var_2 = queue_0.dequeue()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue5.Queue'
    assert f'{type(var_2.head).__module__}.{type(var_2.head).__qualname__}' == 'queue5.Node'
    assert f'{type(var_2.tail).__module__}.{type(var_2.tail).__qualname__}' == 'queue5.Node'
    var_3 = queue_0.dequeue()
    assert queue_0.head is None
    assert queue_0.tail is None
    assert var_2.head is None
    assert var_2.tail is None
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue5.Queue'
    assert var_3.head is None
    assert var_3.tail is None
