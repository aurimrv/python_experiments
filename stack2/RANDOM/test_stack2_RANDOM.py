#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack2/RANDOM/test_stack2.py
import pytest
import stack2 as module_0
import builtins as module_1

def test_case_0():
    stack_0 = module_0.Stack()

def test_case_1():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True

def test_case_2():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True

def test_case_3():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]

def test_case_4():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()

def test_case_5():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True

def test_case_6():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)

def test_case_7():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()

def test_case_8():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    stack_6 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_5 = stack_8.isEmpty()
    assert var_5 is True
    stack_9 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_10 = module_0.Stack()
    var_7 = stack_10.isEmpty()
    assert var_7 is True
    var_8 = stack_10.push(var_7)
    assert stack_10.stack == [True]
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_11 = module_0.Stack()
    var_9 = stack_11.push(set_0)
    stack_12 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_14 = module_0.Stack()

def test_case_9():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False

def test_case_10():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_7 = module_0.Stack()
    var_5 = stack_7.push(set_0)
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_6 = stack_8.push(set_1)
    var_7 = stack_8.isEmpty()
    assert var_7 is False
    var_8 = stack_8.push(stack_5)

def test_case_11():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_4 = stack_6.push(set_0)
    stack_7 = module_0.Stack()

def test_case_12():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'

def test_case_13():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_1 = stack_1.push(set_0)
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_6.__repr__()
    assert var_5 == 'stack:[]'
    stack_7 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_6 = stack_8.push(set_1)
    var_7 = stack_8.isEmpty()
    assert var_7 is False
    stack_9 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    var_9 = stack_9.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    var_11 = stack_11.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    var_13 = stack_13.push(var_12)
    assert stack_13.stack == [True]
    stack_14 = module_0.Stack()
    var_14 = stack_14.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    var_15 = stack_14.isEmpty()
    assert var_15 is True
    var_16 = stack_13.__repr__()
    assert var_16 == 'stack:[True]'

def test_case_14():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_5 = stack_6.push(set_0)
    var_6 = stack_6.isEmpty()
    assert var_6 is False
    var_7 = stack_2.isEmpty()
    assert var_7 is True

def test_case_15():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_5 = stack_7.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_7 = stack_10.isEmpty()
    assert var_7 is True
    stack_11 = module_0.Stack()
    var_8 = stack_11.__repr__()
    assert var_8 == 'stack:[]'
    stack_12 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_13 = module_0.Stack()
    var_9 = stack_13.push(set_0)
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_10 = stack_15.isEmpty()
    assert var_10 is True
    stack_16 = module_0.Stack()
    var_11 = stack_15.isEmpty()
    assert var_11 is True
    stack_17 = module_0.Stack()
    var_12 = stack_17.isEmpty()
    assert var_12 is True
    var_13 = stack_17.push(var_12)
    assert stack_17.stack == [True]
    stack_18 = module_0.Stack()
    var_14 = stack_18.isEmpty()
    assert var_14 is True
    var_15 = var_12.__repr__()
    assert var_15 == 'True'

def test_case_16():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    var_3 = stack_1.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    var_7 = stack_7.__repr__()
    assert var_7 == 'stack:[]'
    stack_8 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    stack_9 = module_0.Stack()
    var_10 = stack_9.isEmpty()
    assert var_10 is True
    stack_10 = module_0.Stack()
    var_11 = stack_9.isEmpty()
    assert var_11 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_12 = stack_12.isEmpty()
    assert var_12 is True
    stack_13 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_14 = module_0.Stack()
    var_13 = stack_14.push(set_1)
    var_14 = stack_8.__repr__()
    assert var_14 == 'stack:[]'

def test_case_17():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    var_4 = stack_2.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    var_6 = stack_4.isEmpty()
    assert var_6 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_8 = module_0.Stack()
    var_8 = stack_8.__repr__()
    assert var_8 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_9 = module_0.Stack()
    var_9 = stack_9.push(set_1)
    var_10 = stack_9.isEmpty()
    assert var_10 is False
    var_11 = stack_4.push(stack_0)

def test_case_18():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(set_0)
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()

def test_case_19():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    var_4 = stack_4.push(var_3)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_6 = module_0.Stack()
    var_6 = stack_6.push(set_1)
    var_7 = stack_6.isEmpty()
    assert var_7 is False
    stack_7 = module_0.Stack()
    var_8 = stack_7.isEmpty()
    assert var_8 is True
    stack_8 = module_0.Stack()
    var_9 = stack_7.isEmpty()
    assert var_9 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    stack_11 = module_0.Stack()
    var_11 = stack_11.__repr__()
    assert var_11 == 'stack:[]'
    stack_12 = module_0.Stack()
    var_12 = stack_12.isEmpty()
    assert var_12 is True
    stack_13 = module_0.Stack()
    var_13 = stack_12.isEmpty()
    assert var_13 is True
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_14 = stack_15.isEmpty()
    assert var_14 is True
    stack_16 = module_0.Stack()
    stack_17 = module_0.Stack()
    var_15 = stack_17.isEmpty()
    assert var_15 is True
    stack_18 = module_0.Stack()
    var_16 = stack_17.isEmpty()
    assert var_16 is True
    stack_19 = module_0.Stack()
    stack_20 = module_0.Stack()
    var_17 = stack_20.isEmpty()
    assert var_17 is True
    var_18 = stack_20.isEmpty()
    assert var_18 is True
    stack_21 = module_0.Stack()

def test_case_20():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_7 = module_0.Stack()
    var_5 = stack_7.push(set_0)
    var_6 = stack_7.isEmpty()
    assert var_6 is False
    var_7 = stack_1.push(stack_7)

def test_case_21():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_1 = stack_1.push(set_0)
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_7 = module_0.Stack()
    var_5 = stack_7.push(set_1)
    var_6 = stack_7.isEmpty()
    assert var_6 is False
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    var_10 = stack_11.push(var_9)
    assert stack_11.stack == [True]
    stack_12 = module_0.Stack()

def test_case_22():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_1 = stack_1.push(set_0)
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_6.__repr__()
    assert var_5 == 'stack:[]'
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_8 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_13 = stack_16.isEmpty()
    assert var_13 is True
    stack_17 = module_0.Stack()
    var_14 = stack_16.isEmpty()
    assert var_14 is True
    stack_18 = module_0.Stack()
    var_15 = stack_18.isEmpty()
    assert var_15 is True
    var_16 = stack_18.push(var_15)
    assert stack_18.stack == [True]
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_19 = module_0.Stack()
    var_17 = stack_19.push(set_1)
    var_18 = stack_19.isEmpty()
    assert var_18 is False
    stack_20 = module_0.Stack()
    stack_21 = module_0.Stack()

def test_case_23():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_10 = module_0.Stack()
    var_7 = stack_10.push(set_0)
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    stack_12 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    stack_13 = module_0.Stack()
    var_10 = stack_13.isEmpty()
    assert var_10 is True
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_14.isEmpty()
    assert var_12 is True
    var_13 = var_8.__repr__()
    assert var_13 == 'True'

def test_case_24():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    var_7 = stack_6.isEmpty()
    assert var_7 is True
    stack_7 = module_0.Stack()

def test_case_25():
    stack_0 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_0 = stack_1.push(set_0)
    var_1 = stack_1.isEmpty()
    assert var_1 is False
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    var_6 = stack_2.__repr__()
    assert var_6 == 'stack:[]'

def test_case_26():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_4 = stack_5.push(set_0)
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()

def test_case_27():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_0)
    stack_2 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    var_4 = stack_2.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_9 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    var_9 = stack_2.__repr__()
    assert var_9 == 'stack:[]'

def test_case_28():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_3 = stack_6.isEmpty()
    assert var_3 is True
    stack_7 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_8 = module_0.Stack()
    var_5 = stack_8.isEmpty()
    assert var_5 is True
    var_6 = stack_8.push(var_5)
    assert stack_8.stack == [True]
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_10 = module_0.Stack()
    var_8 = stack_10.push(set_0)
    var_9 = stack_10.isEmpty()
    assert var_9 is False
    stack_11 = module_0.Stack()
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    var_11 = stack_11.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_14 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_14 = stack_16.isEmpty()
    assert var_14 is True
    stack_17 = module_0.Stack()
    var_15 = stack_17.__repr__()
    assert var_15 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_18 = module_0.Stack()
    var_16 = stack_18.push(set_1)
    stack_19 = module_0.Stack()
    var_17 = stack_19.isEmpty()
    assert var_17 is True
    var_18 = stack_19.isEmpty()
    assert var_18 is True
    stack_20 = module_0.Stack()

def test_case_29():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    var_3 = stack_1.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_5.__repr__()
    assert var_5 == 'stack:[]'
    stack_6 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    var_7 = stack_6.isEmpty()
    assert var_7 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    var_11 = stack_10.push(var_10)
    assert stack_10.stack == [True]
    stack_11 = module_0.Stack()
    var_12 = stack_11.isEmpty()
    assert var_12 is True
    stack_12 = module_0.Stack()
    var_13 = stack_11.isEmpty()
    assert var_13 is True
    stack_13 = module_0.Stack()
    stack_14 = module_0.Stack()
    var_14 = stack_14.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    var_15 = stack_14.isEmpty()
    assert var_15 is True
    stack_16 = module_0.Stack()
    stack_17 = module_0.Stack()
    var_16 = stack_17.isEmpty()
    assert var_16 is True
    stack_18 = module_0.Stack()
    var_17 = stack_12.push(var_14)
    assert stack_12.stack == [True]

def test_case_30():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_8 = stack_10.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_12 = module_0.Stack()
    var_9 = stack_12.push(set_0)
    var_10 = stack_12.isEmpty()
    assert var_10 is False
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_12 = stack_15.isEmpty()
    assert var_12 is True
    var_13 = stack_15.isEmpty()
    assert var_13 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_16 = module_0.Stack()
    var_14 = stack_16.push(set_1)
    stack_17 = module_0.Stack()

def test_case_31():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_7 = stack_8.push(set_1)
    var_8 = stack_8.isEmpty()
    assert var_8 is False
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_11 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    var_12 = stack_12.push(var_11)
    assert stack_12.stack == [True]
    stack_13 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_14 = module_0.Stack()
    var_14 = stack_13.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    var_15 = stack_15.isEmpty()
    assert var_15 is True
    stack_16 = module_0.Stack()
    var_16 = stack_15.isEmpty()
    assert var_16 is True
    stack_17 = module_0.Stack()
    stack_18 = module_0.Stack()
    var_17 = stack_18.isEmpty()
    assert var_17 is True
    stack_19 = module_0.Stack()
    var_18 = stack_19.__repr__()
    assert var_18 == 'stack:[]'
    var_19 = stack_14.isEmpty()
    assert var_19 is True

def test_case_32():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    var_4 = stack_4.push(var_2)
    assert stack_4.stack == [True]

def test_case_33():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    var_5 = stack_4.push(var_4)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    stack_6 = module_0.Stack()
    var_7 = stack_5.isEmpty()
    assert var_7 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    var_9 = stack_9.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    var_10 = stack_9.isEmpty()
    assert var_10 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = var_0.__repr__()
    assert var_12 == 'True'

def test_case_34():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_3 = stack_5.push(set_0)
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    stack_12 = module_0.Stack()
    var_9 = stack_12.__repr__()
    assert var_9 == 'stack:[]'
    stack_13 = module_0.Stack()

def test_case_35():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    var_4 = stack_4.push(var_3)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_8 = stack_10.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_14 = module_0.Stack()
    var_13 = stack_14.push(set_1)
    var_14 = stack_14.isEmpty()
    assert var_14 is False
    set_2 = {var_12, var_10, stack_1, var_6}
    var_15 = stack_4.push(set_2)

def test_case_36():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_7 = module_0.Stack()
    var_7 = stack_7.push(set_0)
    var_8 = stack_7.isEmpty()
    assert var_8 is False
    stack_8 = module_0.Stack()
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    var_10 = stack_8.isEmpty()
    assert var_10 is True
    stack_9 = module_0.Stack()
    var_11 = stack_9.isEmpty()
    assert var_11 is True
    stack_10 = module_0.Stack()
    var_12 = stack_9.isEmpty()
    assert var_12 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_13 = stack_12.isEmpty()
    assert var_13 is True
    stack_13 = module_0.Stack()
    stack_14 = module_0.Stack()
    var_14 = var_8.__repr__()
    assert var_14 == 'False'
    var_15 = var_14.__repr__()
    assert var_15 == "'False'"

def test_case_37():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_6 = stack_9.isEmpty()
    assert var_6 is True
    stack_10 = module_0.Stack()
    var_7 = stack_10.__repr__()
    assert var_7 == 'stack:[]'
    var_8 = var_4.__repr__()
    assert var_8 == 'True'

def test_case_38():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    stack_5 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_4 = stack_6.push(set_0)
    var_5 = stack_6.isEmpty()
    assert var_5 is False
    var_6 = stack_4.__repr__()
    assert var_6 == 'stack:[]'

def test_case_39():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.push(stack_0)

def test_case_40():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.push(stack_0)
    stack_1 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(set_1)
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    var_6 = stack_7.__repr__()
    assert var_6 == 'stack:[]'
    stack_8 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_9 = module_0.Stack()
    var_9 = stack_9.push(set_2)
    var_10 = stack_9.isEmpty()
    assert var_10 is False
    stack_10 = module_0.Stack()
    var_11 = stack_10.isEmpty()
    assert var_11 is True
    var_12 = stack_10.__repr__()
    assert var_12 == 'stack:[]'
    var_13 = stack_10.push(var_12)
    assert stack_10.stack == ['stack:[]']

def test_case_41():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()

def test_case_42():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_4 = stack_5.push(set_0)
    var_5 = stack_5.push(stack_5)
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_6 = module_0.Stack()
    var_6 = stack_6.push(set_1)
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_8 = module_0.Stack()
    var_8 = stack_7.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()

def test_case_43():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.push(stack_0)
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    var_3 = stack_1.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_4 = module_0.Stack()
    var_4 = stack_4.push(set_1)
    stack_5 = module_0.Stack()

def test_case_44():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_1)
    var_3 = stack_1.push(stack_1)
    stack_2 = module_0.Stack()
    var_4 = stack_2.isEmpty()
    assert var_4 is True
    stack_3 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True
    stack_4 = module_0.Stack()
    var_6 = stack_3.isEmpty()
    assert var_6 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_7 = stack_6.isEmpty()
    assert var_7 is True
    stack_7 = module_0.Stack()
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_8 = module_0.Stack()
    var_8 = stack_8.push(set_2)
    stack_9 = module_0.Stack()
    var_9 = stack_9.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    var_10 = stack_9.isEmpty()
    assert var_10 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_15 = module_0.Stack()
    var_13 = stack_15.isEmpty()
    assert var_13 is True
    var_14 = stack_15.push(var_13)
    assert stack_15.stack == [True]
    stack_16 = module_0.Stack()
    var_15 = stack_16.isEmpty()
    assert var_15 is True
    stack_17 = module_0.Stack()
    var_16 = stack_16.isEmpty()
    assert var_16 is True
    stack_18 = module_0.Stack()
    stack_19 = module_0.Stack()
    var_17 = stack_19.isEmpty()
    assert var_17 is True
    stack_20 = module_0.Stack()
    var_18 = stack_20.__repr__()
    assert var_18 == 'stack:[]'
    var_19 = stack_4.push(stack_2)

def test_case_45():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_2 = stack_4.isEmpty()
    assert var_2 is True
    stack_5 = module_0.Stack()
    var_3 = stack_5.__repr__()
    assert var_3 == 'stack:[]'
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_5 = stack_9.isEmpty()
    assert var_5 is True
    stack_10 = module_0.Stack()
    var_6 = stack_9.isEmpty()
    assert var_6 is True
    stack_11 = module_0.Stack()
    var_7 = stack_11.isEmpty()
    assert var_7 is True
    var_8 = stack_11.push(var_7)
    assert stack_11.stack == [True]
    stack_12 = module_0.Stack()
    var_9 = stack_12.isEmpty()
    assert var_9 is True
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_15 = module_0.Stack()
    var_13 = stack_15.isEmpty()
    assert var_13 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_16 = module_0.Stack()
    var_14 = stack_16.push(set_0)
    var_15 = stack_16.isEmpty()
    assert var_15 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_17 = module_0.Stack()
    var_16 = stack_17.push(set_1)
    stack_18 = module_0.Stack()
    var_17 = stack_18.isEmpty()
    assert var_17 is True
    stack_19 = module_0.Stack()
    var_18 = stack_18.isEmpty()
    assert var_18 is True
    stack_20 = module_0.Stack()
    stack_21 = module_0.Stack()
    var_19 = stack_21.isEmpty()
    assert var_19 is True
    stack_22 = module_0.Stack()
    var_20 = stack_11.isEmpty()
    assert var_20 is False

def test_case_46():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.push(stack_0)
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_1)
    stack_2 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_9 = stack_12.isEmpty()
    assert var_9 is True
    stack_13 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_14 = module_0.Stack()
    var_11 = stack_14.isEmpty()
    assert var_11 is True
    var_12 = stack_14.push(var_11)
    assert stack_14.stack == [True]
    stack_15 = module_0.Stack()

def test_case_47():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_5 = stack_6.push(set_0)
    var_6 = var_3.__repr__()
    assert var_6 == 'True'

def test_case_48():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_6.__repr__()
    assert var_5 == 'stack:[]'
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_8 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    var_12 = stack_13.push(var_11)
    assert stack_13.stack == [True]
    stack_14 = module_0.Stack()
    var_13 = stack_14.isEmpty()
    assert var_13 is True
    stack_15 = module_0.Stack()
    var_14 = stack_14.isEmpty()
    assert var_14 is True
    stack_16 = module_0.Stack()
    stack_17 = module_0.Stack()
    var_15 = stack_17.isEmpty()
    assert var_15 is True
    stack_18 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_19 = module_0.Stack()
    var_16 = stack_19.push(set_0)
    var_17 = stack_19.isEmpty()
    assert var_17 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_20 = module_0.Stack()
    var_18 = stack_20.push(set_1)
    var_19 = stack_20.push(stack_20)
    stack_21 = module_0.Stack()
    var_20 = stack_21.isEmpty()
    assert var_20 is True
    stack_22 = module_0.Stack()
    stack_23 = module_0.Stack()

def test_case_49():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_5 = stack_7.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    var_6 = stack_8.__repr__()
    assert var_6 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_9 = module_0.Stack()
    var_7 = stack_9.push(set_1)
    stack_10 = module_0.Stack()
    var_8 = stack_10.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_13 = module_0.Stack()
    stack_14 = module_0.Stack()
    var_11 = stack_14.isEmpty()
    assert var_11 is True
    stack_15 = module_0.Stack()
    var_12 = stack_14.isEmpty()
    assert var_12 is True
    stack_16 = module_0.Stack()
    var_13 = stack_16.isEmpty()
    assert var_13 is True
    var_14 = stack_16.push(var_13)
    assert stack_16.stack == [True]
    var_15 = var_2.__repr__()
    assert var_15 == 'True'

def test_case_50():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_0)
    var_3 = var_0.__repr__()
    assert var_3 == 'True'

def test_case_51():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_3 = stack_5.push(set_0)
    var_4 = stack_5.isEmpty()
    assert var_4 is False
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_5 = stack_8.isEmpty()
    assert var_5 is True
    stack_9 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_10 = module_0.Stack()
    var_7 = stack_10.isEmpty()
    assert var_7 is True
    var_8 = stack_10.push(var_7)
    assert stack_10.stack == [True]
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_10 = stack_13.isEmpty()
    assert var_10 is True
    stack_14 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_12 = stack_16.isEmpty()
    assert var_12 is True
    stack_17 = module_0.Stack()
    var_13 = stack_17.__repr__()
    assert var_13 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_18 = module_0.Stack()
    var_14 = stack_18.push(set_1)
    var_15 = stack_18.push(stack_18)
    stack_19 = module_0.Stack()
    var_16 = stack_19.isEmpty()
    assert var_16 is True
    stack_20 = module_0.Stack()
    var_17 = stack_20.push(var_15)

def test_case_52():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_5 = stack_6.push(set_0)
    var_6 = stack_6.push(stack_6)
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    var_8 = stack_7.isEmpty()
    assert var_8 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_9 = stack_8.push(set_1)
    var_10 = var_7.__repr__()
    assert var_10 == 'True'
    stack_9 = module_0.Stack()
    var_11 = stack_9.isEmpty()
    assert var_11 is True
    stack_10 = module_0.Stack()
    var_12 = stack_7.__repr__()
    assert var_12 == 'stack:[]'

def test_case_53():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = var_0.__repr__()

def test_case_54():
    bytes_0 = b'\xc2\x1fo\x14\xc2\xa9K\xa2j\x84\xd0\x1b\xb5R'
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(bytes_0)

def test_case_55():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_0)
    var_3 = stack_1.isEmpty()
    assert var_3 is False
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_9 = module_0.Stack()
    var_9 = stack_9.push(set_1)
    var_10 = var_7.__repr__()
    assert var_10 == 'True'
    stack_10 = module_0.Stack()
    var_11 = stack_10.isEmpty()
    assert var_11 is True
    stack_11 = module_0.Stack()
    var_12 = var_10.__repr__()
    assert var_12 == "'True'"

def test_case_56():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_4 = stack_5.push(set_0)
    var_5 = stack_5.push(stack_5)
    bytes_0 = b'\xc2\x1fo\x14\xc2\xa9K\xa2j\x84\xd0\x1b\xb5R'
    stack_6 = module_0.Stack()
    var_6 = stack_6.push(bytes_0)
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_8 = stack_8.push(set_1)
    var_9 = var_8.__repr__()
    stack_9 = module_0.Stack()
    var_10 = stack_9.isEmpty()
    assert var_10 is True
    stack_10 = module_0.Stack()
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_11 = module_0.Stack()
    var_11 = stack_11.push(set_2)
    stack_12 = module_0.Stack()
    var_12 = stack_12.isEmpty()
    assert var_12 is True
    stack_13 = module_0.Stack()
    var_13 = stack_12.isEmpty()
    assert var_13 is True
    object_3 = module_1.object()
    set_3 = {object_3, object_3, object_3}
    stack_14 = module_0.Stack()
    var_14 = stack_14.push(set_3)
    var_15 = stack_14.isEmpty()
    assert var_15 is False
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_16 = stack_16.isEmpty()
    assert var_16 is True
    stack_17 = module_0.Stack()
    var_17 = stack_16.isEmpty()
    assert var_17 is True
    stack_18 = module_0.Stack()
    var_18 = stack_18.isEmpty()
    assert var_18 is True
    var_19 = stack_18.push(var_18)
    assert stack_18.stack == [True]
    var_20 = var_1.__repr__()
    assert var_20 == 'True'

def test_case_57():
    bytes_0 = b'\xc2\x1fo\x14\xc2\xa9K\xa2j\x84\xd0\x1b\xb5R'
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(bytes_0)
    stack_1 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_1 = stack_2.push(set_0)
    var_2 = stack_2.push(stack_2)
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    var_6 = stack_7.__repr__()
    assert var_6 == 'stack:[]'
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    var_10 = stack_11.push(var_9)
    assert stack_11.stack == [True]
    stack_12 = module_0.Stack()
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_14 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_14 = stack_16.isEmpty()
    assert var_14 is True
    stack_17 = module_0.Stack()
    stack_18 = module_0.Stack()
    var_15 = stack_18.isEmpty()
    assert var_15 is True
    stack_19 = module_0.Stack()
    var_16 = stack_18.isEmpty()
    assert var_16 is True
    stack_20 = module_0.Stack()
    var_17 = stack_20.isEmpty()
    assert var_17 is True
    var_18 = stack_20.isEmpty()
    assert var_18 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_21 = module_0.Stack()
    var_19 = stack_21.push(set_1)
    stack_22 = module_0.Stack()

def test_case_58():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_3 = module_0.Stack()
    var_3 = stack_3.push(set_0)
    var_4 = var_3.__repr__()
    stack_4 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    var_6 = stack_4.__repr__()
    assert var_6 == 'stack:[]'

def test_case_59():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_1 = stack_2.push(set_0)
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_5 = stack_8.push(set_1)
    var_6 = stack_8.isEmpty()
    assert var_6 is False
    stack_9 = module_0.Stack()
    var_7 = stack_6.isEmpty()
    assert var_7 is True

def test_case_60():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_2 = stack_1.push(set_0)
    var_3 = var_0.__repr__()
    assert var_3 == 'True'
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    var_7 = stack_5.push(var_6)
    assert stack_5.stack == [True]
    stack_6 = module_0.Stack()
    var_8 = stack_6.isEmpty()
    assert var_8 is True
    var_9 = stack_6.isEmpty()
    assert var_9 is True
    var_10 = var_7.__repr__()

def test_case_61():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_0 = stack_2.isEmpty()
    assert var_0 is True
    stack_3 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_4 = module_0.Stack()
    var_2 = stack_4.isEmpty()
    assert var_2 is True
    var_3 = stack_4.push(var_2)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_7 = module_0.Stack()
    var_5 = stack_7.push(set_0)
    var_6 = stack_7.push(stack_7)
    stack_8 = module_0.Stack()

def test_case_62():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_1 = stack_3.isEmpty()
    assert var_1 is True
    stack_4 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    var_4 = stack_5.push(var_3)
    assert stack_5.stack == [True]
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_6 = module_0.Stack()
    var_5 = stack_6.push(set_0)
    var_6 = stack_6.isEmpty()
    assert var_6 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_7 = module_0.Stack()
    var_7 = stack_7.push(set_1)
    var_8 = stack_7.push(stack_7)
    stack_8 = module_0.Stack()
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    var_10 = stack_8.isEmpty()
    assert var_10 is True
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_9 = module_0.Stack()
    var_11 = stack_9.push(set_2)
    var_12 = var_9.__repr__()
    assert var_12 == 'True'
    stack_10 = module_0.Stack()
    var_13 = stack_10.isEmpty()
    assert var_13 is True
    stack_11 = module_0.Stack()
    var_14 = stack_10.isEmpty()
    assert var_14 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_15 = stack_13.isEmpty()
    assert var_15 is True
    stack_14 = module_0.Stack()
    var_16 = stack_14.__repr__()
    assert var_16 == 'stack:[]'
    object_3 = module_1.object()
    set_3 = {object_3, object_3, object_3}
    stack_15 = module_0.Stack()
    var_17 = stack_15.push(set_3)
    var_18 = stack_9.pop()
    assert stack_9.stack == []

def test_case_63():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_64():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True

def test_case_65():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True

def test_case_66():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True

def test_case_67():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    var_4 = stack_4.push(var_3)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    var_6 = stack_5.isEmpty()
    assert var_6 is True

def test_case_68():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(set_0)
    var_3 = stack_2.isEmpty()
    assert var_3 is False
    stack_3 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_3.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_11 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    var_12 = stack_12.push(var_11)
    assert stack_12.stack == [True]
    stack_13 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_14 = module_0.Stack()
    var_14 = stack_13.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_15 = stack_16.isEmpty()
    assert var_15 is True
    stack_17 = module_0.Stack()
    var_16 = stack_17.__repr__()
    assert var_16 == 'stack:[]'
    stack_18 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_19 = module_0.Stack()
    var_17 = stack_19.push(set_1)

def test_case_69():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    stack_12 = module_0.Stack()
    var_9 = stack_12.__repr__()
    assert var_9 == 'stack:[]'
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_13 = module_0.Stack()
    var_10 = stack_13.push(set_0)
    with pytest.raises(Exception):
        stack_10.pop()

def test_case_70():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    stack_12 = module_0.Stack()
    var_9 = stack_12.__repr__()
    assert var_9 == 'stack:[]'
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_13 = module_0.Stack()
    var_10 = stack_13.push(set_0)
    var_11 = stack_13.isEmpty()
    assert var_11 is False
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_12 = stack_15.isEmpty()
    assert var_12 is True
    stack_16 = module_0.Stack()
    var_13 = stack_15.isEmpty()
    assert var_13 is True
    stack_17 = module_0.Stack()
    var_14 = stack_17.isEmpty()
    assert var_14 is True
    var_15 = stack_17.push(var_14)
    assert stack_17.stack == [True]
    stack_18 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_19 = module_0.Stack()
    var_16 = stack_19.push(set_1)

def test_case_71():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_7 = module_0.Stack()
    var_5 = stack_7.push(set_1)
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_6 = stack_9.isEmpty()
    assert var_6 is True
    stack_10 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    var_9 = stack_11.push(var_8)
    assert stack_11.stack == [True]
    stack_12 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_13 = module_0.Stack()
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_12 = stack_15.isEmpty()
    assert var_12 is True
    stack_16 = module_0.Stack()
    var_13 = stack_16.__repr__()
    assert var_13 == 'stack:[]'
    stack_17 = module_0.Stack()
    var_14 = stack_17.isEmpty()
    assert var_14 is True
    var_15 = stack_17.isEmpty()
    assert var_15 is True
    none_type_0 = None

def test_case_72():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_4 = module_0.Stack()
    var_4 = stack_4.push(set_0)
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    stack_6 = module_0.Stack()
    var_7 = stack_6.isEmpty()
    assert var_7 is True
    stack_7 = module_0.Stack()
    var_8 = stack_6.isEmpty()
    assert var_8 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_9 = stack_8.push(set_1)
    var_10 = stack_8.isEmpty()
    assert var_10 is False
    stack_9 = module_0.Stack()
    var_11 = stack_9.isEmpty()
    assert var_11 is True
    stack_10 = module_0.Stack()
    var_12 = stack_9.isEmpty()
    assert var_12 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_13 = stack_12.isEmpty()
    assert var_13 is True
    stack_13 = module_0.Stack()
    var_14 = stack_13.__repr__()
    assert var_14 == 'stack:[]'
    stack_14 = module_0.Stack()
    var_15 = stack_14.isEmpty()
    assert var_15 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_16 = stack_16.isEmpty()
    assert var_16 is True
    stack_17 = module_0.Stack()
    var_17 = stack_16.isEmpty()
    assert var_17 is True
    stack_18 = module_0.Stack()
    stack_19 = module_0.Stack()
    var_18 = stack_19.isEmpty()
    assert var_18 is True
    stack_20 = module_0.Stack()

def test_case_73():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    var_6 = stack_6.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_8 = stack_11.isEmpty()
    assert var_8 is True
    stack_12 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_13 = module_0.Stack()
    var_10 = stack_13.push(set_0)
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_11 = stack_15.isEmpty()
    assert var_11 is True
    stack_16 = module_0.Stack()
    var_12 = stack_15.isEmpty()
    assert var_12 is True
    stack_17 = module_0.Stack()
    var_13 = stack_17.isEmpty()
    assert var_13 is True
    var_14 = stack_17.push(var_13)
    assert stack_17.stack == [True]
    var_15 = stack_3.__repr__()
    assert var_15 == 'stack:[]'

def test_case_74():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True

def test_case_75():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    var_4 = stack_4.push(var_3)
    assert stack_4.stack == [True]
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_9 = module_0.Stack()
    var_8 = stack_8.isEmpty()
    assert var_8 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_10 = stack_13.isEmpty()
    assert var_10 is True
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    with pytest.raises(Exception):
        stack_10.pop()

def test_case_76():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_5 = stack_8.isEmpty()
    assert var_5 is True
    stack_9 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_10 = module_0.Stack()
    var_7 = stack_10.isEmpty()
    assert var_7 is True
    var_8 = stack_10.push(var_7)
    assert stack_10.stack == [True]
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_9 = stack_12.isEmpty()
    assert var_9 is True
    stack_13 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_11 = stack_15.isEmpty()
    assert var_11 is True
    stack_16 = module_0.Stack()
    var_12 = stack_16.__repr__()
    assert var_12 == 'stack:[]'
    stack_17 = module_0.Stack()
    var_13 = stack_17.isEmpty()
    assert var_13 is True
    var_14 = stack_17.isEmpty()
    assert var_14 is True
    var_15 = stack_7.push(stack_12)

def test_case_77():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_3 = stack_6.isEmpty()
    assert var_3 is True
    stack_7 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_8 = module_0.Stack()
    var_5 = stack_8.isEmpty()
    assert var_5 is True
    var_6 = stack_8.push(var_5)
    assert stack_8.stack == [True]
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_9 = module_0.Stack()
    var_7 = stack_9.push(set_0)
    stack_10 = module_0.Stack()
    var_8 = stack_10.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_12 = module_0.Stack()
    var_10 = stack_12.isEmpty()
    assert var_10 is True
    var_11 = stack_12.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_14 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_14 = stack_16.isEmpty()
    assert var_14 is True
    stack_17 = module_0.Stack()
    var_15 = stack_17.__repr__()
    assert var_15 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_18 = module_0.Stack()
    var_16 = stack_18.push(set_1)
    var_17 = stack_18.isEmpty()
    assert var_17 is False
    with pytest.raises(Exception):
        stack_2.pop()

def test_case_78():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_3 = module_0.Stack()
    var_3 = stack_3.push(set_1)
    var_4 = stack_3.isEmpty()
    assert var_4 is False
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_5 = stack_5.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    var_6 = stack_5.isEmpty()
    assert var_6 is True
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    var_8 = stack_7.push(var_7)
    assert stack_7.stack == [True]
    stack_8 = module_0.Stack()
    var_9 = stack_8.isEmpty()
    assert var_9 is True
    stack_9 = module_0.Stack()
    var_10 = stack_8.isEmpty()
    assert var_10 is True
    stack_10 = module_0.Stack()
    stack_11 = module_0.Stack()
    var_11 = stack_11.isEmpty()
    assert var_11 is True
    stack_12 = module_0.Stack()
    var_12 = stack_12.__repr__()
    assert var_12 == 'stack:[]'
    stack_13 = module_0.Stack()
    var_13 = stack_13.isEmpty()
    assert var_13 is True
    stack_14 = module_0.Stack()
    var_14 = stack_13.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_15 = stack_16.isEmpty()
    assert var_15 is True
    stack_17 = module_0.Stack()
    stack_18 = module_0.Stack()
    var_16 = stack_18.isEmpty()
    assert var_16 is True
    stack_19 = module_0.Stack()
    with pytest.raises(Exception):
        stack_14.pop()

def test_case_79():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = stack_0.isEmpty()
    assert var_1 is False
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    var_3 = stack_2.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_4 = stack_5.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    var_5 = stack_6.__repr__()
    assert var_5 == 'stack:[]'
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    with pytest.raises(Exception):
        stack_1.pop()

def test_case_80():
    stack_0 = module_0.Stack()
    stack_1 = module_0.Stack()
    var_0 = stack_1.isEmpty()
    assert var_0 is True
    stack_2 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    var_3 = stack_3.push(var_2)
    assert stack_3.stack == [True]
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_6 = stack_7.isEmpty()
    assert var_6 is True
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_7 = stack_9.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    stack_11 = module_0.Stack()
    stack_12 = module_0.Stack()
    var_9 = stack_12.isEmpty()
    assert var_9 is True
    stack_13 = module_0.Stack()
    var_10 = stack_13.__repr__()
    assert var_10 == 'stack:[]'
    stack_14 = module_0.Stack()
    var_11 = stack_14.isEmpty()
    assert var_11 is True
    stack_15 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_16 = module_0.Stack()
    var_12 = stack_16.push(set_0)
    var_13 = stack_16.isEmpty()
    assert var_13 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_17 = module_0.Stack()
    var_14 = stack_17.push(set_1)
    stack_18 = module_0.Stack()
    var_15 = stack_18.isEmpty()
    assert var_15 is True
    var_16 = stack_18.isEmpty()
    assert var_16 is True
    stack_19 = module_0.Stack()
    var_17 = stack_19.isEmpty()
    assert var_17 is True
    stack_20 = module_0.Stack()
    var_18 = stack_19.isEmpty()
    assert var_18 is True

def test_case_81():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_82():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_1 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(set_0)
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_5 = stack_6.isEmpty()
    assert var_5 is True
    stack_7 = module_0.Stack()
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_6 = stack_8.push(set_1)
    var_7 = stack_8.push(stack_8)
    stack_9 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    stack_10 = module_0.Stack()
    var_9 = stack_9.isEmpty()
    assert var_9 is True

def test_case_83():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_84():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    stack_2 = module_0.Stack()
    var_1 = stack_2.isEmpty()
    assert var_1 is True
    stack_3 = module_0.Stack()
    var_2 = stack_2.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_5 = stack_7.isEmpty()
    assert var_5 is True
    stack_8 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_9 = module_0.Stack()
    var_6 = stack_9.push(set_0)
    var_7 = stack_9.isEmpty()
    assert var_7 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_10 = module_0.Stack()
    var_8 = stack_10.push(set_1)
    stack_11 = module_0.Stack()
    var_9 = stack_11.isEmpty()
    assert var_9 is True
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True
    stack_15 = module_0.Stack()
    var_13 = stack_15.isEmpty()
    assert var_13 is True
    var_14 = stack_15.push(var_13)
    assert stack_15.stack == [True]

def test_case_85():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True

def test_case_86():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(set_0)
    var_3 = stack_2.push(stack_2)

def test_case_87():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True

def test_case_88():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    stack_5 = module_0.Stack()
    var_3 = stack_5.isEmpty()
    assert var_3 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_4 = stack_7.isEmpty()
    assert var_4 is True
    var_5 = stack_7.isEmpty()
    assert var_5 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_8 = module_0.Stack()
    var_6 = stack_8.push(set_0)
    var_7 = stack_8.isEmpty()
    assert var_7 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_9 = module_0.Stack()
    var_8 = stack_9.push(set_1)
    stack_10 = module_0.Stack()
    var_9 = stack_10.isEmpty()
    assert var_9 is True
    stack_11 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    stack_13 = module_0.Stack()
    var_11 = stack_13.isEmpty()
    assert var_11 is True
    stack_14 = module_0.Stack()
    var_12 = stack_14.__repr__()
    assert var_12 == 'stack:[]'
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_13 = stack_16.isEmpty()
    assert var_13 is True
    stack_17 = module_0.Stack()
    var_14 = stack_16.isEmpty()
    assert var_14 is True

def test_case_89():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_4 = module_0.Stack()
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_5 = module_0.Stack()
    var_5 = stack_5.push(set_0)
    var_6 = stack_5.isEmpty()
    assert var_6 is False
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_6 = module_0.Stack()
    var_7 = stack_6.push(set_1)
    var_8 = stack_6.push(stack_6)
    stack_7 = module_0.Stack()
    var_9 = stack_7.isEmpty()
    assert var_9 is True
    stack_8 = module_0.Stack()
    var_10 = stack_7.isEmpty()
    assert var_10 is True
    stack_9 = module_0.Stack()
    stack_10 = module_0.Stack()
    var_11 = stack_10.isEmpty()
    assert var_11 is True
    stack_11 = module_0.Stack()
    var_12 = stack_11.__repr__()
    assert var_12 == 'stack:[]'
    stack_12 = module_0.Stack()
    var_13 = stack_12.isEmpty()
    assert var_13 is True
    stack_13 = module_0.Stack()
    var_14 = stack_13.isEmpty()
    assert var_14 is True
    stack_14 = module_0.Stack()
    var_15 = stack_13.isEmpty()
    assert var_15 is True
    stack_15 = module_0.Stack()
    stack_16 = module_0.Stack()
    var_16 = stack_16.isEmpty()
    assert var_16 is True
    stack_17 = module_0.Stack()
    stack_18 = module_0.Stack()
    stack_19 = module_0.Stack()
    stack_20 = module_0.Stack()
    var_17 = stack_20.isEmpty()
    assert var_17 is True
    stack_21 = module_0.Stack()
    var_18 = stack_20.isEmpty()
    assert var_18 is True
    stack_22 = module_0.Stack()
    var_19 = stack_22.isEmpty()
    assert var_19 is True
    var_20 = stack_22.push(var_19)
    assert stack_22.stack == [True]
    with pytest.raises(Exception):
        stack_20.pop()

def test_case_90():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_3 = stack_4.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    var_4 = stack_5.__repr__()
    assert var_4 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_6 = module_0.Stack()
    var_5 = stack_6.push(set_1)
    var_6 = stack_6.isEmpty()
    assert var_6 is False

def test_case_91():
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True
    stack_1 = module_0.Stack()
    var_1 = stack_0.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_4.__repr__()
    assert var_3 == 'stack:[]'

def test_case_92():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.isEmpty()
    assert var_1 is True
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_2 = stack_3.isEmpty()
    assert var_2 is True
    stack_4 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    stack_5 = module_0.Stack()
    stack_6 = module_0.Stack()
    var_4 = stack_6.isEmpty()
    assert var_4 is True
    stack_7 = module_0.Stack()
    var_5 = stack_7.__repr__()
    assert var_5 == 'stack:[]'
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_8 = module_0.Stack()
    var_6 = stack_8.push(set_1)
    var_7 = stack_8.isEmpty()
    assert var_7 is False
    stack_9 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    var_9 = stack_9.isEmpty()
    assert var_9 is True
    stack_10 = module_0.Stack()
    var_10 = stack_10.isEmpty()
    assert var_10 is True
    var_11 = stack_10.isEmpty()
    assert var_11 is True
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_11 = module_0.Stack()
    var_12 = stack_11.push(set_2)
    var_13 = var_10.__repr__()
    assert var_13 == 'True'
    stack_12 = module_0.Stack()
    var_14 = stack_12.isEmpty()
    assert var_14 is True
    stack_13 = module_0.Stack()
    var_15 = stack_12.isEmpty()
    assert var_15 is True
    stack_14 = module_0.Stack()
    stack_15 = module_0.Stack()
    var_16 = stack_15.isEmpty()
    assert var_16 is True
    stack_16 = module_0.Stack()
    object_3 = module_1.object()
    set_3 = {object_3, object_3, object_3}
    stack_17 = module_0.Stack()
    var_17 = stack_17.push(set_3)
    var_18 = var_17.__repr__()
    with pytest.raises(Exception):
        stack_10.pop()

def test_case_93():
    stack_0 = module_0.Stack()
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_1 = module_0.Stack()
    var_0 = stack_1.push(set_0)
    var_1 = stack_1.isEmpty()
    assert var_1 is False
    bytes_0 = b'\xc2\x1fo\x14\xc2\xa9K\xa2j\x84\xd0\x1b\xb5R'
    stack_2 = module_0.Stack()
    var_2 = stack_2.push(bytes_0)
    stack_3 = module_0.Stack()
    var_3 = stack_3.isEmpty()
    assert var_3 is True
    var_4 = stack_3.isEmpty()
    assert var_4 is True
    stack_4 = module_0.Stack()
    var_5 = stack_4.isEmpty()
    assert var_5 is True
    stack_5 = module_0.Stack()
    var_6 = stack_4.isEmpty()
    assert var_6 is True
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    var_7 = stack_7.isEmpty()
    assert var_7 is True
    stack_8 = module_0.Stack()
    stack_9 = module_0.Stack()
    var_8 = stack_9.isEmpty()
    assert var_8 is True
    var_9 = stack_9.isEmpty()
    assert var_9 is True
    object_1 = module_1.object()
    set_1 = {object_1, object_1, object_1}
    stack_10 = module_0.Stack()
    var_10 = stack_10.push(set_1)
    var_11 = var_8.__repr__()
    assert var_11 == 'True'
    stack_11 = module_0.Stack()
    var_12 = stack_11.isEmpty()
    assert var_12 is True
    stack_12 = module_0.Stack()
    var_13 = stack_11.isEmpty()
    assert var_13 is True
    stack_13 = module_0.Stack()
    stack_14 = module_0.Stack()
    var_14 = stack_14.isEmpty()
    assert var_14 is True
    stack_15 = module_0.Stack()
    var_15 = stack_15.__repr__()
    assert var_15 == 'stack:[]'
    stack_16 = module_0.Stack()
    var_16 = stack_16.isEmpty()
    assert var_16 is True
    stack_17 = module_0.Stack()
    object_2 = module_1.object()
    set_2 = {object_2, object_2, object_2}
    stack_18 = module_0.Stack()
    var_17 = stack_18.push(set_2)
    var_18 = stack_18.push(stack_18)
    stack_19 = module_0.Stack()
    stack_20 = module_0.Stack()
    var_19 = stack_20.isEmpty()
    assert var_19 is True
    stack_21 = module_0.Stack()
    var_20 = stack_20.isEmpty()
    assert var_20 is True
    stack_22 = module_0.Stack()
    var_21 = stack_22.isEmpty()
    assert var_21 is True
    var_22 = stack_22.push(var_21)
    assert stack_22.stack == [True]
    stack_23 = module_0.Stack()

def test_case_94():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(set_0)
    var_1 = var_0.__repr__()
    stack_1 = module_0.Stack()
    var_2 = stack_1.isEmpty()
    assert var_2 is True
    stack_2 = module_0.Stack()
    var_3 = stack_1.isEmpty()
    assert var_3 is True
    stack_3 = module_0.Stack()
    stack_4 = module_0.Stack()
    var_4 = stack_4.isEmpty()
    assert var_4 is True
    stack_5 = module_0.Stack()
    var_5 = stack_5.__repr__()
    assert var_5 == 'stack:[]'
    stack_6 = module_0.Stack()
    stack_7 = module_0.Stack()
    stack_8 = module_0.Stack()
    var_6 = stack_8.isEmpty()
    assert var_6 is True
    stack_9 = module_0.Stack()
    var_7 = stack_8.isEmpty()
    assert var_7 is True
    stack_10 = module_0.Stack()
    var_8 = stack_10.isEmpty()
    assert var_8 is True
    var_9 = stack_10.push(var_8)
    assert stack_10.stack == [True]
    stack_11 = module_0.Stack()
    var_10 = stack_11.isEmpty()
    assert var_10 is True
    stack_12 = module_0.Stack()
    var_11 = stack_11.isEmpty()
    assert var_11 is True
    stack_13 = module_0.Stack()
    var_12 = stack_13.isEmpty()
    assert var_12 is True

def test_case_95():
    none_type_0 = None
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True