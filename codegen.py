import sys, getopt
import csv
import qrcode


def readAndPrintFile(inputFileName, outputFilename):
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
    thisQRpair = readAndPrintFile(inputFileName, outputFilename)

if __name__ == '__main__':
    main((sys.argv[1:]))