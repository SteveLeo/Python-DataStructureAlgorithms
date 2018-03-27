'''
GPA Calculator
Python script in subsection 1.1.2 of Goodrich, etal (2013, pp.3)
'''

print('Welcome to the GPA CAlulator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')

# Map from letter grade to point value
points = {'A+': 4.00, 'A': 4.00, 'A-': 3.67, 
		  'B+': 3.33, 'B': 3.00, 'B-': 2.67,
		  'C+': 2.33, 'C': 2.00, 'C-': 1.67,
		  'D+': 1.33, 'D': 1.00, 'F': 0.00}

num_courses = 0
total_points = 0
done = False

while not done:
	grade = input()

	if grade == '':
		done = True
	elif grade not in points:
		print("Unknown grade '{0}' being ignored.".format(grade))
	else:
		num_courses += 1
		total_points += points[grade]

if num_courses > 0:
	print("Your GPA is {0:.3}".format(total_points/num_courses))