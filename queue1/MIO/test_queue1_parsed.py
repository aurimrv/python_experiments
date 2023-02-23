#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/queue1/MIO/test_queue1.py
import pytest
import queue1 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()
    var_1 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    var_2 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 2
    var_3 = queue_0.__str__()
    var_4 = queue_0.__str__()
    var_5 = var_3.__str__()
    var_6 = queue_0.__len__()
    assert var_6 == 2
    var_7 = queue_0.dequeue()
    assert len(queue_0) == 1
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'queue1.Queue'
    assert len(var_7) == 1

def test_case_1():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_2():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    var_1 = queue_0.peek()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue1.Queue'
    assert len(var_1) == 1
    var_2 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 2
    assert len(var_1) == 2
    var_3 = queue_0.__str__()
    var_4 = queue_0.__str__()
    var_5 = var_3.__str__()
    var_6 = var_1.clear()
    assert len(queue_0) == 0
    assert len(var_1) == 0
    var_7 = queue_0.__len__()
    assert var_7 == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_3():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0

def test_case_4():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_5():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_6():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.clear()
    var_2 = var_1.__str__()
    var_3 = var_2.__str__()
