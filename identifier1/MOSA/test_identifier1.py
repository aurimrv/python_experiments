# Automatically generated by Pynguin.
import pytest
import identifier1 as module_0


def test_case_0():
    identifier_0 = module_0.Identifier()
    str_0 = "H9"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True


def test_case_1():
    identifier_0 = module_0.Identifier()
    str_0 = "f"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True


def test_case_2():
    identifier_0 = module_0.Identifier()
    str_0 = "6E"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False


def test_case_3():
    identifier_0 = module_0.Identifier()


def test_case_4():
    identifier_0 = module_0.Identifier()
    str_0 = "6j"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False


def test_case_5():
    identifier_0 = module_0.Identifier()
    str_0 = "j{"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False


def test_case_6():
    identifier_0 = module_0.Identifier()
    str_0 = "g$"
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "e6v"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True
    identifier_1 = module_0.Identifier()
    module_0.Identifier(*identifier_1, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "e6zLE"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True
    str_1 = ""
    var_1 = identifier_0.validateIdentifier(str_1)
    assert var_1 is False
    var_0.valid_f(var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "z*"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.valid_s(str_0)
    assert var_0 is False
    identifier_1 = module_0.Identifier()
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: str_0}
    module_0.Identifier(*list_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "e6iczLE"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    str_1 = ")f"
    var_1 = identifier_0.validateIdentifier(str_1)
    assert var_1 is False
    var_0.valid_f(var_0)
