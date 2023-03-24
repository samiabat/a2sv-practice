import pytest
from arthimetic_operations import ArthimeticClass
'test_arthimetic_operations.py'
class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
    def test_substract(self ):
        # arrange
        x, y = 3.0, 2.0
        expected_output = 1.0
        # act
        actual_output = ArthimeticClass.subtract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("3", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(3, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("3", "2")
        
        assert expected_output == actual_output
    def test_multipy(self ):
        # arrange
        x, y = 3.0, 2.0
        expected_output = 6.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("3", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(3, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("3", "2")
        
        assert expected_output == actual_output
    def test_devide(self ):
        # arrange
        x, y = 6.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("6", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(6, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("6", "2")
        
        assert expected_output == actual_output
    
        
 
