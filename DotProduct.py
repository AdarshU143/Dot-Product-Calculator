# 2 vector dot product calculator

vector1 = input("Enter a the values of a vector seperated by a space\n").split()

vector2= input("Enter the values of a second vector seperated by a space\n").split()
#recieves two vectors

end = int(len(vector1))

for i in range(0, end):
    vector1[i] = int(vector1[i])
    vector2[i] = int(vector2[i])
#turns vector lists values into integers

hold = 0
vector_product = []

for i in range(0, end):
    hold = vector1[i] * vector2[i]
    vector_product.append(hold)
#multiplies the x,y,z components of the vectors together

dot_product = 0

for i in range(0, end):
    dot_product = dot_product + vector_product[i]
#sums up the dot product


print("The dot product of ", vector1,"and ", vector2,"is\n____________________________________________\n")
print(dot_product)


