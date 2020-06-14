
# -----  mutable list  ------
language = ['python', 'java', 'cpp', 'groovy', 'kotlin', 'js']

# get(index)
print(language[0]) 

# get length
print(len(language))

# add last
language.append('swift')
print(language)

# get and remove last
print(language.pop())
print(language)

# delete index
language.pop(1) # delete 'java'
print(language)

# replace index
language[1] = 'c#' # cpp -> c#
print(language)

# -----  tuple, immutable list, read only  ------
family = ('mother', 'father', 'wife')
print(family)

# only one element
t = (1,)
print(t)



