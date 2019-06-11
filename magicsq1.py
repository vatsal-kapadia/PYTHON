 # for odd order magic squares
def oddmagsq():
    a = n // 2
    b = n - 1
    mat[a][b] = 1

    for i in range(2, n ** 2 + 1):
        a = a - 1
        b = b + 1
        if (a == -1 and b != n):
            a = n - 1
        elif (b == n and a != -1):
            b = 0
        elif (a == -1 and b == n):
            a = 0
            b = n - 2

        # condition for position which is already occupied
        if mat[a][b] != 0:
            a = a + 1
            b = b - 2

        mat[a][b] = a

    print("The magic square is: ")
    for i in range(n):
        print(mat[i])

# for even order magic squares divisible by 4

def dubevenmagsq():
    
    # adding the numbers from 1 to n**2 in the matrix
    for x in range(n):
        for y in range(n):
            mat[x][y]= n*a+b+1

    """The values of elements in matrices of order n/4 by n/4 at all four corners of the square and in middle matrix of order n/2 by n/2 are altered
    """

    for x in range(n//4):
        for y in range(n//4):
            mat[x][y] = (n * n + 1) - mat[x][y]

    for x in range(n//4):
        for y in range(3*n//4,n):
            mat[x][y] = (n * n + 1) - mat[x][y]

    for x in range(3*n//4,n):
        for y in range(n//4):
            mat[a][b] = (n * n + 1) - mat[x][y]

    for x in range(3*n//4,n):
        for y in range(3*n//4,n):
            mat[x][y] = (n * n + 1) - mat[x][y]

    for x in range(n//4,3*n//4):
        for y in range(n//4,3*n//4):
            mat[x][y] = (n * n + 1) - mat[x][y]

    print("The magic square is:")
    for x in range(n):
        print(mat[x])




n=int(input("Enter a number "))
print("The magic sum is %d " %(n*(n**2+1)//2))
mat=[]
for p in range(n):
    mat.append([])
for p in range(n):
    for q in range(n):
        mat[p].append(q)
        # initialise all elements to zero
        mat[p][q]=0

if(n%2!=0):
    oddmagsq()
elif(n%4==0):
    dubevenmagsq()