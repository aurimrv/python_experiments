#Pyguin test cases converted from /home/lucca/desktop/ic/experimento/testes/python_experiments/sort1/MOSA/test_sort1.py
import pytest
import sort1 as module_0

def test_case_0():
    bytes_0 = b'\x1d\xb6\x17\xd9e\xf0?v'
    sort_0 = module_0.Sort()

def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
    var_1 = sort_0.selection_sort(list_0)
    sort_1 = module_0.Sort()

def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_3():
    sort_0 = module_0.Sort()
    str_0 = 'Z^[`[*-KJ8P&'
    sort_1 = module_0.Sort()
    var_0 = sort_1.merge_sort(str_0)

def test_case_4():
    bool_0 = True
    sort_0 = module_0.Sort()

def test_case_5():
    list_0 = []
    sort_0 = module_0.Sort(*list_0)

def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    bool_1 = False
    var_0 = sort_0.quick_sort(list_0, bool_1, bool_0)

def test_case_7():
    dict_0 = {}
    list_0 = []
    sort_0 = module_0.Sort(*list_0)
    var_0 = sort_0.merge_sort(list_0)
    none_type_0 = None
    sort_1 = module_0.Sort()
    var_1 = sort_1.merge(dict_0, none_type_0)

def test_case_8():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
    str_0 = 'Z^[`[*-KJ8P&'
    float_0 = 659.5920854829486
    dict_0 = {}
    var_1 = sort_0.insertion_sort(dict_0)
    var_2 = sort_0.merge(str_0, var_1)
