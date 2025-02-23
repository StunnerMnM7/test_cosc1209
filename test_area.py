import pytest  
from area import calculate_area_square

def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-80)  

def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("80")  

def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([80])  
        
def test_calculate_area_square_failure():  
    assert calculate_area_square(80) == 160
