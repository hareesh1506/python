import pytest


class C:
    def f(self):
        return 1
    def g(self):
        return 2
# """
def test_f():
    c=C()
    assert c.f() == 1

def test_g():
    c=C()
    assert c.g() == 2

# """

#
"""
fixture= it is a decorator used to decarate a function with pytest.fixture
futures of fixers

prac_1
@pytest.fixture
def c_instance():
    return C()
def test_f(c_instance):
    assert c_instance.f() == 1
    print('test-1')

def test_g(c_instance):
    assert c_instance.g() == 2
    print('test-2')
"""

#
# import pytest
# import tempfile
#
# @pytest.fixture()
# def c_instance():
#     return C()
#
# @pytest.fixture()
# def temporary_dir():
#     with tempfile.TemporaryDirectory() as tmpdir:
#         yield tmpdir
#
#
# def test_f(c_instance,temporary_dir):
#     assert c_instance.f() == 1
#     print(temporary_dir)
#

