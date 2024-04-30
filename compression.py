import zipfile

#https://docs.python.org/3/library/zipfile.html

#fileOperations
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
# "r" - Read - opens a file for read access only

#create a file with some data
f = open("test.txt", "a")
f.write("testtesttesttesttesttest")
f.close()

# create a zipfile object and add a file in the path to the archive
#archiveName = 'test.zip'
#myZip = zipfile.ZipFile(archiveName, mode='x')
#myZip.write(filename='test.txt', arcname=archiveName)
#myZip.close

with zipfile.ZipFile('spam.zip', 'w') as myzip:
    myzip.write('test.txt')

### These operations are just testing out some of the compression lib functionality

#import zlib

#f = open('test2.txt', "w")
#f.write("another test")
#f.close

#f = open('test.txt')
#objData = f.read()
#print(objData)
#f.close

#f = open('test2.txt', "r")
#objData2 = f.read()
#print(objData2)
#f.close

#objData3 = objData + objData2
#print(objData3)

#compressedData = zlib.compress(bytes(objData3, 'utf-8'))
#f = open('data.zip', 'x')
#f.write(compressedData)
#f.close

