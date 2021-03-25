
import pytest

@pytest.mark.smoke
def test_login():
    print("Login page")

@pytest.mark.Regression
def test_AddProduct():
    print("Add Product")

@pytest.mark.smoke
def test_logout():
    print("Logout page")