import numpy as np
import pyhyp.pythag

def test_add_nums():
    '''Test for the pythag function that adds numbers'''

    # Specify the input and expected output variables
    test_variable_a = 3.5
    test_variable_b = 4.8
    expected_output = 8.3

    # Act
    output = pyhyp.pythag.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output

def test_add_array_nums():
    '''Test for the pythag function that adds numbers for arrays'''
    
    test_arr_a = np.array([23,56,123])
    test_arr_b = np.array([43,67,105])
    
    exp_out = np.array([66,123,228])
    
    # Act
    output = pyhyp.pythag.add_nums(test_arr_a, test_arr_b)

    # Assert
    assert np.allclose(output,exp_out)
    
def test_square_num():
    '''Test for the pythag function that squares numbers'''
    test_a = 25
        
    exp_out = 625
    
    # Act
    output = pyhyp.pythag.square_num(test_a)

    # Assert
    assert output == exp_out
    
def test_array_square_num():
    '''Test for the pythag function that squares numbers for arrays'''
    
    test_arr_a = np.array([5.5,8,9.1])
    
    exp_out = np.array([5.5**2,64,9.1**2])
    
    output = pyhyp.pythag.square_num(test_arr_a)
    
    assert np.allclose(exp_out,output)    

def test_square_root():
    '''Test for the pythag sq rt function'''
    test_a = 25
        
    exp_out = 5
    
    # Act
    output = pyhyp.pythag.square_root(test_a)

    # Assert
    assert output == exp_out

def test_array_square_root():
    '''Test for the pythag sq rt function for arrays'''
    
    test_arr_a = np.array([16,25,121])
    
    exp_out = np.array([4,5,11])
    
    output = pyhyp.pythag.square_root(test_arr_a)
    
    assert np.allclose(exp_out,output)
    
def test_calc_hyp():
    '''Integration test for calc_hyp'''
    
    test_a = 9.82
    test_b = 15.23
    
    exp_out = 18.1
    
    output = pyhyp.pythag.calc_hyp(test_a,test_b)
    
    assert np.allclose(exp_out,output,atol=1e-1)
    
def test_arr_calc_hyp():
    '''Integration test for calc_hyp'''
    
    test_arr_a = np.array([9.82,123,78])
    test_arr_b = np.array([15.23,45,26.83])
    
    exp_out = np.array([18.1,130.9,82.4])
    
    output = pyhyp.pythag.calc_hyp(test_arr_a,test_arr_b)
    
    assert np.allclose(exp_out,output,rtol=1e-2)