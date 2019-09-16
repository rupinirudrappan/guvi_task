import collections

input_list=[3,5,[3,56],3,'guvi',[3,7,'zen',4.6],5,2,'pit']

max=0

sub_list=[]

for i in input_list:

	if isinstance(i, collections.Iterable) and not isinstance(i, (str)):
		sub_list.append(i)

print(len(sub_list))

max_list=[]

for i in sub_list:

	if max<len(i):

		max=len(i)
		max_list=i

print(max_list)

print(input_list.index(max_list))


    