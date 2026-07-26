import sys
 

print("length ", sys.argv[1])
print("interview persona ", sys.argv[2])
print("difficulty level ", sys.argv[3])
print("number of selects ", sys.argv[4])

maxargu = int(sys.argv[4]) + 5
print(maxargu)

for i in range(5,maxargu):
    print(sys.argv[i])
    i+=1