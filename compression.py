import zlib

#fileOperations
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f = open("test.txt", "a")
f.write("test")
f.close()

f = open('test2.txt', "w")
f.write("another test")
f.close

f = open('test.txt')
objData = f.read()
print(objData)
f.close

f = open('test2.txt', "r")
objData2 = f.read()
print(objData2)
f.close

objData3 = objData + objData2
print(objData3)

compressedData = zlib.compress(bytes(objData3, 'utf-8'))
f = open('data.zip', 'x')
f.write(compressedData)
f.close

#https://docs.python.org/3/library/zipfile.html
