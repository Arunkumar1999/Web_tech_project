def display(height):
	import matplotlib
	import matplotlib.pyplot as plt 

	# x-coordinates of left sides of bars 
	left = [1, 2, 3,4,5] 

	# heights of bars 
	# height = [10, 24, 36] 

	# labels for bars 
	tick_label = ['preform', 'label', 'cap','carton','tape'] 

	# plotting a bar chart 
	plt.bar(left, height, tick_label = tick_label, 
			width = 0.8, color = ['red', 'green','blue','yellow','orange']) 

	# naming the x-axis 
	plt.xlabel('x - axis') 
	# naming the y-axis 
	plt.ylabel('y - axis') 
	# plot title 
	plt.title('My bar chart!') 

	# function to show the plot 
	# plt.show() 
	plt.savefig("result.png", bbox_inches='tight')
	return 1