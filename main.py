def triangle_lower(r):
    for i in range(1, r + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()   
        
def triangle_upper(r):
    for i in range(r, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()  
        
def pyramid(r):
    for i in range(1, r + 1):
        spaces = " " * (r - i)
        print(spaces, end=" ")
        for j in range(1,2 *  i):
            print("*", end=" ")
        print()    
        
r = 5
triangle_lower(r)
print()
triangle_upper(r)
print()
pyramid(r)    