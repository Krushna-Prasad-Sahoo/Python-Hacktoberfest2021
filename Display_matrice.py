a=[]
n=int(input())
print("Enter the element ::>")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print(a)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(a[i][j], end=" ")                  #new line
   print()
b=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    b.append(row)
print(b)

