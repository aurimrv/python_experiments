#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/stack2/MIO/test_stack2.py
import pytest
import stack2 as module_0

def test_case_0():
    bool_0 = True
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(bool_0)
    stack_1 = module_0.Stack()
    with pytest.raises(Exception):
        stack_1.pop()

def test_case_1():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
    var_1 = stack_0.push(var_0)
    var_2 = stack_0.pop()
    assert len(stack_0.stack) == 1

def test_case_2():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False

def test_case_3():
    stack_0 = module_0.Stack()
    var_0 = stack_0.__repr__()
    assert var_0 == 'stack:[]'
    var_1 = stack_0.isEmpty()
    assert var_1 is True
