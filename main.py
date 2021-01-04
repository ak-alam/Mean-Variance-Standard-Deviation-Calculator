import mean_var_std

#testing it using different values
#test value one 
test_lst = [0,1,2,3,4,5,6,7,8]
print("Result of test list one")
test_one = mean_var_std.calculate(test_lst)
print(test_one)
print("--------------------------------------------------------------")

#test value two 
test_lst = [2,6,2,8,4,0,1,5,7]
print("Result of test list two")
test_one = mean_var_std.calculate(test_lst)
print(test_one)


print("--------------------------------------------------------------")
#test value three 
test_lst = [9,1,5,3,3,3,2,9,0]
print("Result of test list three")
test_one = mean_var_std.calculate(test_lst)
print(test_one)


print("--------------------------------------------------------------")
#test value four 
test_lst = [2,6,2,8,4,0,1,]
print("Result of test list four")
test_one = mean_var_std.calculate(test_lst)
print(test_one)
