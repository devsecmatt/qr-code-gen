import sys, getopt
import csv
import qrcode
import zipfile
import os
from qreader import QReader
import cv2

def qrCodeVerify(filepath):
    if(filepath):
        filePath=filepath
    else:
        filePath=('qr-code-images')
    directoryContents = os.listdir(filePath)
    for image in directoryContents:
        qreader = QReader()
        # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(filePath+ "/" +image), cv2.COLOR_BGR2RGB)
        # Use the detect_and_decode function to get the decoded QR data
        decoded_text = qreader.detect_and_decode(image=image)
        print(decoded_text)

def addToZip(archive='qr-codes.zip', file2add=None):
    filePath = 'qr-code-images'
    directoryContents = os.listdir(filePath)
    for imageFile in directoryContents:
        with zipfile.ZipFile(archive, 'w') as myzip:
            myzip.write(filePath + "/" + imageFile)

def readAndPrintFile(inputFileName):
    with open(inputFileName) as csvFile:
        qrReader = csv.reader(csvFile, delimiter=",")
        for row in qrReader:
            thisQRfilename=row[0]
            thisQRurl=row[1]
            genQRcode([thisQRfilename, thisQRurl])

def genQRcode(thisQRpair):
    dir = "qr-code-images/"
    img = qrcode.make(thisQRpair[1])
    myImageName = thisQRpair[0]+".png"
    img.save(dir+myImageName)

def main(argv):
    inputFileName = 'code-list.csv'
    outputFilename = 'qr-codes.zip'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["input=","output"])
    except getopt.GetoptError:
        print("codegen.py -i <inputfile> -o <outputfile")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("codegen.py -i <inputfile> -o <outputfile")
        elif opt in ("-i", "--input"):
            inputFilename = arg
        elif opt in ('-o', "--ofile"):
            outputFilename = arg
    thisQRpair = readAndPrintFile(inputFileName)
    compressedQRcodes = addToZip(archive=outputFilename)
    qrCodeVerify(filepath='qr-code-images')


if __name__ == '__main__':
    main((sys.argv[1:]))