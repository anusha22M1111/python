#class 7
#22mia1111

#in a supermarket there are two sections s1 and s2 the sales details of item1 to item_n of section1
and item1 to itemp

L1=[]
L2=[]
N=int(input())
M=int(input())
for i in range(N):
    L1.append(input())
for i in range(M):
    L2.append(input())
L1.extend(L2)
L1.sort()
print(L1)

L1.split(",")


#sunny and johnny together have m dollars they want to spend on ice cream.
#the parlor offers n flavors aand they want to choose two flavors so that they end up spending
#the whole amount.
#you are given the cost of these flavors the cost of the ith flavor is denoted by ci
#you have to display the indices of the two flacors whose sum

N=[30,40,50,20,60]
n=len(N)
M=int(input())
for i in range(n-1):
    for j in range((i+1),n):
        if N[i]+N[j]==M:
            print(i)
            print(j)

#list comprehension
L=[input() for i in range(3)]
print(L)

#two dimentional matrix

M1=[[1,2,3],[4,5,6],[7,8,9]]
r=int(input())
c=int(input())
list1=[[int(input()) for j in range(c)]for i in range(r)]
list2=[[int(input()) for j in range(c)]for i in range(r)]
print(list1)
print(list2)

summat=[[list1[i][j]+list2[i][j] for j in range(c)]for i in range(r)]
print(summat)
for x in summat:
    print(x)


#givrn a positions of coins of player1 and player2 in a 3x3 tic tac toc board write a program to ,
#determine if the board position is a solution and if so identify the winner of
#the game. in a tic tac toc problem,if the coins in a row or column or along a
#diagonal is of the same player then he has won the game .Assume

board=[[int(input()) for j in range(3)]for i in range(3)]

for i in range(3):
    if(board[i][0]==1 and board[i][1]==1 and  board[i][2]==1):
        print("player 1 is the winner")
    elif(board[i][1]==2 and board[i][2]==2 and  board[i][0]==2):
        print("player 2 is the winner")
        
for j in range(3):
    if(board[1][j]==1 and board[2][j]==1 and  board[0][j]==1):
        print("player 1 is the winner")
    elif(board[1][j]==2 and board[2][j]==2 and  board[0][j]==2):
        print("player 2 is the winner")
        
if(board[0][0]==1 and board[1][1]==1 and  board[2][2]==1):
    print("player 1 is the winner")
elif(board[0][0]==2 and board[1][1]==2 and  board[2][2]==2):
    print("player 2 is the winner")
    
if(board[2][0]==1 and board[1][1]==1 and  board[0][2]==1):
    print("player 1 is the winner")
elif(board[2][0]==2 and board[1][1]==2 and  board[0][2]==2):
    print("player 2 is the winner")
