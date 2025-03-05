#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

filename = 'task03.txt'
file = open(filename,'r')
data = file.read()
print(data)

#also google helped me out with data.strip, which removes extra whitespaces from the start and end of the data
b = data.strip().split('\n\n')

large = 0

for a in b:
    
    #map is pretty cool when you want to apply a function to every item in an iterable list. 
    #https://stackoverflow.com/questions/69573663/how-to-iterate-over-a-list-of-lists-using-pythons-map-function

    highscore = list(map(int, a.split()))
    
    x = sum(highscore)
    
    if x > large:
        large = x

print("The largest sum is:", large)



