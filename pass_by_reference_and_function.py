def numbers_less_than_twenty(list):
  counter = 0
  initial_list=[]
  while counter < len(list):
    item = list[counter]
    initial_list.append(list[counter])
    if item > 20:
      list.remove(item)
    else:
      counter+= 1
  print(initial_list)  
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)