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

clusters = data.strip().split('\n\n')

large = 0

for cluster in clusters:
    
    points = list(int, cluster.split())
    
    x = sum(points)
    
    if x > large:
        large = x

print("The largest sum is:", large)



