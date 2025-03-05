#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numbers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.
"""



def target(lvl,ac):    
    lvl = input("Enter the level of fighter: ")
    ac = input("Enter the armor class (AC): ")

    filename = 'task03.txt'
    file = open(filename,'r')
    rows = file.read()

    level = int(lvl)
    armorclass = int(ac)
  
    ac = list(range(10, -11, -1))
    
    row = rows[level - 1].split()
  
    ac_index = ac.index(armorclass)
    target_number = row[ac_index]
    
    print(f"To hit AC {armorclass} at level {level}, you need: {target_number}")

    return 

def tests():
    assert target(3,7) == 23
    assert target(9,-1) == 17
    assert target(13,-10) == 20

if __name__=="__main__":
    tests()