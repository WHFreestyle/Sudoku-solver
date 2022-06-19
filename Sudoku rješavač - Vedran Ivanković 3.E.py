
##next move when its done with searching put a random number in a spot 

print("SUDOKU RJEŠAVAČ")
print("Upiši po jedan red sudoka kojeg želiš rješenog i klikni enter")
print("Za prazna polja upiši 0")
print("Primjer za upis jedan od redova: 0 0 0 1 2 3 0 4 0")
print("Upiši prvi red:")
print()
row1 = list(map(int,input().split()))
print("Upiši drugi red:")
print()
row2 = list(map(int,input().split()))
print("Upiši treći red:")
print()
row3 = list(map(int,input().split()))
print("Upiši četvrti red:")
print()
row4 = list(map(int,input().split()))
print("Upiši peti red:")
print()
row5 = list(map(int,input().split()))
print("Upiši šesti red:")
print()
row6 = list(map(int,input().split()))
print("Upiši sedmi red:")
print()
row7 = list(map(int,input().split()))
print("Upiši osmi red:")
print()
row8 = list(map(int,input().split()))
print("Upiši deveti red:")
print()
row9 = list(map(int,input().split()))

grid = [row1
        ,row2
        ,row3
        ,row4
        ,row5
        ,row6
        ,row7
        ,row8
        ,row9]


def provjeri(y,x,grid):
    global num_miss
    print(num_miss)
    temp = []
    for i in range(0,9):
        if grid[y][i] not in temp:
            temp.append(grid[y][i])
        if grid[i][x] not in temp:
            temp.append(grid[i][x])
  
        
    pocetak_x = x - x%3
    pocetak_y = y-y%3
    for i in range(0,3):
        for j in range(0,3):
            if grid[pocetak_y+i][pocetak_x+j] not in temp:
                temp.append(grid[pocetak_y+i][pocetak_x+j])
    temp.remove(0)
    
    if len(temp) == 8:
        
        for i in range(1,10):
            if i not in temp:
                grid[y][x] = i
                num_miss=0
##        for i in range(9):
##            for j in range(9):
##                print(grid[i][j],end = " ")
##            print()
##        print()
    
    num_miss+=1 
    return

def prov_kocke(y,x,grid):
    
    pocetak_x = x*3
    pocetak_y = y*3
    slobodni = []
    slobodni_temp = []
    free_nums = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            if grid[pocetak_y+i][pocetak_x+j] in free_nums:
                free_nums.remove(grid[pocetak_y+i][pocetak_x+j])
            if grid[pocetak_y+i][pocetak_x+j] == 0:
                slobodni.append([pocetak_y+i,pocetak_x+j])
    
    for s in slobodni:
        temp=[]
        for i in range(0,9):
            if grid[s[0]][i] not in temp:
                temp.append(grid[s[0]][i])
            if grid[i][s[1]] not in temp:
                temp.append(grid[i][s[1]])
        if 0 in temp:
            temp.remove(0)
        slobodni_temp.append(temp)
    for i in range(1,10):
        tmp = 0
        for j in range(0,len(slobodni)):
            if i in slobodni_temp[j]:
                tmp+=1
            if tmp == len(slobodni)-1 and i in free_nums:
                free_nums.remove(i)
                for z in range(0,len(slobodni)):
                
                    if i not in slobodni_temp[z]:
                        temp_y = slobodni[z][0]
                        temp_x = slobodni[z][1]
                        
                        grid[temp_y][temp_x]=i
##                        for f in range(9):
##                            for g in range(9):
##                                print(grid[f][g],end = " ")
##                            print()
##                        print()
                        
                        
                      
    return
    


gotovo = False
num_miss=0
while not gotovo:
    gotovo = True
    for i in range(0,9):
        if 0 in grid[i]:
            gotovo = False
    
    if num_miss < 83:
        for i in range(0,9):
            for j in range(0,9):
                if grid[i][j] == 0:
                    provjeri(i,j,grid)
    else:
        for i in range(0,3):
            for j in range(0,3):
                num_miss=0
                prov_kocke(i,j,grid)
        

for i in range(9):
        for j in range(9):
            print(grid[i][j],end = " ")
        print()
