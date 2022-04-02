import pickle

# pickly dumps and loads for serialize and deserialize objects in Python.


# myset1 = {1, 3, 4, 5}

# val= pickle.dumps(myset1)
# print(val)

# val2 = pickle.loads(val)
# print(val2)


# pickly can serialize function. 
def add(x,y):
    print(x +y)
    
# val3 = pickle.dumps(add)   #using only fucntion name
# print(val3)

# data = pickle.loads(val3)
# data(5,6)


# pickle write function(with print) in a file resolve the print issue


# file1 = open("text.txt", "wb")

# pickle.dump(add, file1)   # addd function name first then file 

# file1.close()


# pickle loads a file

file2 = open("text.txt", "rb")

data = pickle.load(file2)

print(type(data))

data(12, 6)