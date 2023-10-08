original_lst = [10,2,98,-34,-56,-21,-89,765,8910]
new_list = [pow(i,2) for i in original_lst if i < 0]
print(new_list)