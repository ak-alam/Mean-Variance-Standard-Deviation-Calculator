import numpy as np

def calculate(list):
  
  try:
      #converting list into 3X3 matrix	
      num_array = np.array(list).reshape(3,3)
        
      #calculating mean across Row, column and mean of matrix
      mean_row = num_array.mean(axis = 0).tolist() 
      mean_col = num_array.mean(axis = 1).tolist()
      mean_val = num_array.mean()
      #calculating variance across rows, column and variance of matrix
      vari_row = num_array.var(axis = 0).tolist()
      vari_col = num_array.var(axis = 1).tolist()
      variance = num_array.var()
      #standard deviation calculating standard deviation across Row, column and standard deviation of matrix
      sd_row = num_array.std(axis = 0).tolist() 
      sd_col = num_array.std(axis = 1).tolist()
      sd =  num_array.std()
      #calculating maximum across Row, column and maximun of matrix
      max_row = num_array.max(axis = 0).tolist() 
      max_col = num_array.max(axis = 1).tolist() 
      maximum = num_array.max()
      #calculating minimum across Row, column and minimum of matrix
      min_row = num_array.min(axis=0).tolist() 
      min_col = num_array.min(axis=1).tolist() 
      minimum = num_array.min()
      #calculating sum across Row, column and sum of matrix
      sum_row = num_array.sum(axis=0).tolist()
      sum_col = num_array.sum(axis=1).tolist()
      sum_val = num_array.sum()
      #converting the result into a dictionary value  
      calulation = {'mean': [mean_row, mean_col, mean_val],
             'variance': [vari_row, vari_col, variance],
             'standard deviation': [sd_row, sd_col, sd],
             'max' : [max_row, max_col, maximum],
             'min' : [min_row, min_col, minimum],
             'sum' : [sum_row, sum_col, sum_val]
             }
      return calulation
  except ValueError:
    print('List must contain nine numbers.')
