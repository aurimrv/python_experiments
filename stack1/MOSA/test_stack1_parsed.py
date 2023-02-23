#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/stack1/MOSA/test_stack1.py
import pytest
import stack1 as module_0

def test_case_0():
    str_0 = '0'
    var_0 = module_0.postfix_eval(str_0)
    assert var_0 == 0

def test_case_1():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.pop()

def test_case_2():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.peek()

def test_case_3():
    str_0 = 'Q[?#\\\')"v":\tCX|(x'
    stack_node_0 = module_0.StackNode(str_0)
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_4():
    str_0 = 't)z?xNb)'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_5():
    bytes_0 = b'\x1a8\xa3\x01x\x91\xd5'
    str_0 = '`=r'
    var_0 = module_0.check_parenthesis(bytes_0)
    assert var_0 is True
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_6():
    str_0 = "X(@\\>u'G"
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_7():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0

def test_case_8():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_0 = stack_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    var_1 = stack_0.push(none_type_0)
    assert len(stack_0) == 1

def test_case_9():
    str_0 = 'PceQCCbe'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_10():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_0 = stack_0.push(stack_0)
    assert len(stack_0) == 1
    bytes_0 = b'\xd8'
    var_1 = stack_0.push(var_0)
    assert len(stack_0) == 2
    str_0 = 'f)yj'
    stack_1 = module_0.Stack()
    assert len(stack_1) == 0
    var_2 = module_0.check_parenthesis(bytes_0)
    assert var_2 is True
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_11():
    str_0 = ')'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_1 = stack_0.push(var_0)
    assert len(stack_0) == 1
    var_2 = stack_0.peek()
    assert var_2 is False
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_12():
    str_0 = '+'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_13():
    str_0 = 'Q[?]J)"v":\tX|(x'
    str_1 = '+'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_1)
