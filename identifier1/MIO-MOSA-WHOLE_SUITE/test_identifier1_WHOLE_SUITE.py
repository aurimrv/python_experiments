#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/identifier1/WHOLE_SUITE/test_identifier1.py.orig
import pytest
import identifier1 as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    identifier_0 = module_0.Identifier()
    str_0 = 'N~P{c=2s'
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    identifier_1 = module_0.Identifier()

def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    identifier_0 = module_0.Identifier()

def test_case_2():
    list_0 = []
    str_0 = "y\n(s/i'#!\x0b46WuH\x0cixuN"
    dict_0 = {str_0: str_0, str_0: str_0}
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(list_0)
    assert var_0 is False

def test_case_3():
    str_0 = '0K!fWZ1Nj^m$>7s'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_4():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = []
    identifier_0 = module_0.Identifier(*list_0)
    list_1 = []
    identifier_1 = module_0.Identifier(*list_1)

def test_case_5():
    str_0 = 'dYjOEfJ'
    identifier_0 = module_0.Identifier()
    identifier_1 = module_0.Identifier()
    identifier_2 = module_0.Identifier()
    var_0 = identifier_2.valid_f(str_0)
    assert var_0 is True
    var_1 = identifier_1.validateIdentifier(str_0)
    assert var_1 is False

def test_case_6():
    str_0 = 'u'
    bytes_0 = b'~P%d\x99S'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True

def test_case_7():
    bytes_0 = b'.`i\xeb\x0f'
    list_0 = [bytes_0]
    dict_0 = {}

def test_case_8():
    object_0 = module_1.object()
    int_0 = 2545
    str_0 = "}#Ys%@&Kx,u=M)6'V"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.valid_s(str_0)
    assert var_0 is False

def test_case_9():
    str_0 = '1~'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    str_1 = 'T}'

def test_case_10():
    dict_0 = {}
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(dict_0)
    assert var_0 is False

def test_case_11():
    pass
