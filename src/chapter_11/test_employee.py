# Ganesha

from employee import Employee
import pytest


@pytest.fixture
def get_emp_instance():
    emp = Employee('Ganesha', 'Kailas', 10000)
    return emp

def test_give_default_raise():
    emp = Employee('Ganesha', 'Kailas', 10000)
    assert emp.salary == 10000
    emp.give_raise()
    assert emp.salary == 15000
    

def test_give_custom_raise():
    emp = Employee('Ganesha', 'Kailas', 10000)
    assert emp.salary == 10000
    emp.give_raise(10000)
    assert emp.salary == 20000


def test_give_default_raise_using_fixture(get_emp_instance):
    emp = get_emp_instance
    assert emp.salary == 10000
    emp.give_raise()
    assert emp.salary == 15000
    
def test_give_custom_raise_using_fixture(get_emp_instance):
    emp = get_emp_instance
    assert emp.salary == 10000
    emp.give_raise(10000)
    assert emp.salary == 20000
