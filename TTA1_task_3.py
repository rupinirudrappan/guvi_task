courses = {'python': 1500, 'java': 1000, 'c': 800, 'c++': 1200}

new_courses=sorted(courses.items(), key = lambda x : x[1])

print(new_courses)