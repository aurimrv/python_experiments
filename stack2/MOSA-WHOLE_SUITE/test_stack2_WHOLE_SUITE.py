#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack2/WHOLE_SUITE/test_stack2.py.orig
import pytest
import stack2 as module_0

def test_case_0():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.push(stack_1)
    var_1 = stack_1.pop()
    assert stack_1.stack == []
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack2.Stack'
    assert var_1.stack == []
    stack_2 = module_0.Stack()
    var_2 = var_1.push(var_1)
    var_3 = var_1.isEmpty()
    var_4 = stack_1.__repr__()
    assert var_4 == 'stack:[stack:[...]]'

def test_case_1():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_2():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_3():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.__repr__()
    assert var_0 == 'stack:[]'

def test_case_4():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.__repr__()
    assert var_0 == 'stack:[]'
    list_0 = [stack_1, stack_0, var_0, var_0]
    var_1 = stack_1.push(list_0)
    var_2 = stack_1.push(stack_0)

def test_case_5():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_6():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()
