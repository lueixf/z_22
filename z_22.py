input_data = open('input.txt', 'r') 
data = input_data.read()
a = int(data)
b =bin(a)
k = 0
for i in range(1, len(b)):
    if b[i] == '1':
        k+=1
output_data = open('output.txt','w')
output_data.write(str(k))
input_data.close()
output_data.close()