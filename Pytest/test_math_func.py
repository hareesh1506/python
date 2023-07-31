import math_func
import pytest
import sys
"""
@pytest.mark.number
# @pytest.mark.skip(reason="do not run number and test")
# @pytest.mark.skipif(sys.version_info < (3, 10), reason='i dont want to run this test case...')
def test_add():
    assert math_func.add(5,8) == 13
    assert math_func.add(6,4) == 10
    assert math_func.add(7,3) == 10
    # print(math_func.add(5,8),'--------------------------------------')

@pytest.mark.number
def test_prod():
    assert math_func.prod(5,5) == 25
    assert math_func.prod(3,3) == 9
    assert math_func.prod(2,2) == 4
    assert math_func.prod(2,3) <= 20
    assert math_func.prod(2,1) >=1
    assert math_func.prod(2,2) != 3

@pytest.mark.strings
def test_add_string():
    result= math_func.add('hello','harish')
    assert result == 'helloharish'
    assert type(result) is str
    assert 'hello' in result
    assert 'world' not in result

@pytest.mark.string
def test_prod_string():
    result = math_func.prod('hello',3)
    assert result == 'hellohellohello'
    assert result is not str
    assert 'hello' in result
    assert 'world' not in result
"""


#
# print('test-1')
# def test_add():
#     assert math_func.add(5,8) == 13
#     assert math_func.add(6,4) == 10
#     assert math_func.add(7,3) == 10
#
# def test_prod():
#     assert math_func.prod(5,5) == 25
#     assert math_func.prod(3,3) == 9
#     assert math_func.prod(2,2) == 4
#     assert math_func.prod(2,3) <= 20
#     assert math_func.prod(2,1) >=1
#     assert math_func.prod(2,2) != 3
#
#
# def test_add_string():
#     result= math_func.add('hello','harish')
#     assert result == 'helloharish'
#     assert type(result) is str
#     assert 'hello' in result
#     assert 'world' not in result
#
# def test_prod_string():
#     result = math_func.prod('hello',3)
#     assert result == 'hellohellohello'
#     assert result is not str
#     assert 'hello' in result
#     assert 'world' not in result

# CODE
"""
import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/path/to/chrome'
    chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options
"""



