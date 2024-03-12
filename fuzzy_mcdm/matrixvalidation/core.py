## Parameter check

# from . import consistency
import numpy as np

class Matrix_check:
    
    def __init__(self, criteria_names, alternative_names, matrix_per_criteria, criteria_comparison, custom_inconsistency=0.1):
        self.criteria_names=criteria_names
        self.alternative_names=alternative_names
        self.matrix_per_criteria=matrix_per_criteria
        self.criteria_comparison=criteria_comparison
        self.inconsistency=custom_inconsistency
        self.check_redundancy=0
        
        #dimention and the consistency will be checked on the spot
        self.check_dimentions_and_dtype()
        print("Everything is fine")
    def check_dimentions_and_dtype(self):
        #check for any value assigned as none
#         if self.criteria_names==None or self.alternative_names==None or self.matrix_per_criteria==None or type(self.criteria_comparison)!=np.ndarray or self.inconsistency==None:
#             self.check_redundancy=1
#             raise ValueError("Cannot assign None as input.")
        
        #--------------------------------------------------------
        
        #check for dtype
        if type(self.criteria_names)!=list:
            self.check_redundancy=1
            raise ValueError("The criterias must be a list of string.")
        #check if every element in the array is string
        for ele in self.criteria_names:
            if type(ele)!=str:
                self.check_redundancy=1
                raise ValueError("Element in the criteria list is not string.")
        
        #do the same for self.alternative_names
        if type(self.alternative_names)!=list:
            self.check_redundancy=1
            raise ValueError("The alternatives must be a list of string.")
        #check if every element in the array is string
        for ele in self.alternative_names:
            if type(ele)!=str:
                self.check_redundancy=1
                raise ValueError("Element in the alternative list is not string.")
            
        #find the length of self.criteria_names and self.alternative_names
        
        criteria_len=len(self.criteria_names)
        alternative_len=len(self.alternative_names)
        
        #--------------------------------------------------------
        
        
        #check whether each element is numpy array or not
        
        if type(self.matrix_per_criteria)!=np.ndarray:
            self.check_redundancy=1
            raise ValueError("Element in the matrix_per_criteria is not numpy array.")
            
        if self.matrix_per_criteria.ndim!=3:
            self.check_redundancy=1
            raise ValueError("The dimention of the element in matrix_per_criteria is not 3D.")
            
        if self.matrix_per_criteria.shape[0]!=criteria_len or self.matrix_per_criteria.shape[1]!=alternative_len or self.matrix_per_criteria.shape[2]!= alternative_len:
            self.check_redundancy=1
            raise ValueError(f"The shape of the element in matrix list of criteria is not correct. It should be ({criteria_len}, {alternative_len}, {alternative_len})")
            
        #every guy must have value > 0
        if (self.matrix_per_criteria <= 0).any():
            self.check_redundancy=1
            raise ValueError("The element in the matrix list of criteria must have value greater than 0")
            
            
        ## ***check whether the matrix provided has transpose element reciprocal of each other***
            
            
        #finally for the last guy
        if type(self.criteria_comparison)!=np.ndarray:
            self.check_redundancy=1
            raise ValueError("The criteria comparision is not numpy array.")
        if self.criteria_comparison.ndim!=1 and self.criteria_comparison.ndim!=2:
            self.check_redundancy=1
            raise ValueError("The dimention of the element in criteria comparision is not 1D/2D.")
            
        
        if self.criteria_comparison.ndim==1:
            if self.criteria_comparison.shape[0]!=criteria_len:
                self.check_redundancy=1
                raise ValueError("The number of element in criteria comparision is not correct")
        
        
        if self.criteria_comparison.ndim==2:
            if self.criteria_comparison.shape[0]!=criteria_len or self.criteria_comparison.shape[1]!=criteria_len:
                self.check_redundancy=1
                raise ValueError("The row or columns of the element in criteria comparision is not correct.")
        #every guy must have value>0
        if (self.criteria_comparison <= 0).any():
            self.check_redundancy=1
            raise ValueError("The element in the criteria comparision must have value greater than 0")
         ## ***check whether the matrix provided has transpose element reciprocal of each other***
    def check_consistency(self):
        pass

