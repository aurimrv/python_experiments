#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/queue1/WHOLE_SUITE/test_queue1.py
import pytest
import queue1 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.peek()

def test_case_1():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_2():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.clear()

def test_case_3():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.clear()

def test_case_4():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_0.__str__()

def test_case_5():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    var_1 = queue_0.dequeue()
    assert len(queue_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue1.Queue'
    assert len(var_1) == 0
    var_2 = queue_0.enqueue(var_1)
    assert len(queue_0) == 1
    assert len(var_1) == 1
    var_3 = queue_0.dequeue()
    assert len(queue_0) == 0
    assert len(var_1) == 0
    assert len(var_3) == 0
    var_4 = queue_0.peek()
    var_5 = queue_0.enqueue(var_3)
    assert len(queue_0) == 1
    assert len(var_1) == 1
    assert len(var_3) == 1
    var_6 = var_3.dequeue()
    assert len(queue_0) == 0
    assert len(var_1) == 0
    assert len(var_3) == 0
    assert len(var_6) == 0
    var_7 = var_6.clear()
    var_8 = var_6.__len__()
    assert var_8 == 0
    bool_0 = False
    queue_node_0 = module_0.QueueNode(bool_0)

def test_case_6():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.clear()
    var_1 = queue_1.clear()

def test_case_7():
    bool_0 = False
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(bool_0)
    assert len(queue_0) == 1

def test_case_8():
    complex_0 = -855.07 + 3693.73564j
    queue_node_0 = module_0.QueueNode(complex_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    var_1 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 2

def test_case_9():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_node_0 = module_0.QueueNode(queue_0)
    assert len(queue_node_0.data) == 0
    var_0 = queue_1.enqueue(queue_0)
    assert len(queue_1) == 1
    var_1 = queue_1.peek()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue1.Queue'
    assert len(var_1) == 0
    var_2 = queue_0.__len__()
    assert var_2 == 0
    var_3 = queue_1.__str__()
