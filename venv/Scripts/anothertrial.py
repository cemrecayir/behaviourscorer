# Original list
individualScore = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
 
# iterate through the sublist using List comprehension
flatList = [element for innerList in individualScore for element in innerList]
 
# printing original list
print('List', individualScore)
# printing flat list
print('Flat List', flatList)