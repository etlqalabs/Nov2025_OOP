import pytest


@pytest.fixture()
def setup_1():
    print("Before test step fix -1..")
    yield
    print("After test step fix -1 ..")

@pytest.fixture()
def setup_2():
    print("Before test step..fix 2")
    yield
    print("After test step..fix 2")

def test_compare_number_1(setup_1,setup_2):
    print("test case 1 started...")
    assert 1 == 1, "Mismatched data"
    print("test case 1 completed...")



'''
def test_compare_number_2(setup_2,setup_1):
    print("test case 2 started...")
    assert 2 == 2, "Mismatched data"
    print("test case 2 completed...")



def test_compare_number_3():
    print("test case 3 started...")
    assert 3 == 3, "Mismatched data"
    print("test case 3 completed...")
'''