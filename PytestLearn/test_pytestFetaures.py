import pytest
import pytest_check as check


# Hard Assertion fails and terminate the test
def test_compare_numbers_hardAssert():
    assert 1 == 1,"mismatched test 1"
    print("test 1 passed")
    assert 1 == 2, "mismatched test 2"
    print("test 2 passed")
    assert 2 == 2, "mismatched test test 3"
    print("test 3 passed")




# soft Assertion fails and terminate the test
def test_compare_numbers_softAssert():
    #assert 1 == 1,"mismatched test 1"
    check.is_true(1==1,"mismatched test 1")
    print("test 1 passed")
    #assert 1 == 2, "mismatched test 2"
    check.is_true(1 == 2, "mismatched test 2")
    check.is_true(1 == 5, "mismatched test 4")
    print("test 2 passed")
    #assert 2 == 2, "mismatched test test 3"
    check.equal(2, 2, "mismatched test 2")
    print("test 3 passed")