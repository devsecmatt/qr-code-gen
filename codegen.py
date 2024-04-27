import csv
import qrcode

def readAndPrintFile(fileName):
    with open(fileName) as csvFile:
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

def main():
    fileName = 'code-list.csv'
    thisQRpair = readAndPrintFile(fileName)
    #genQRcode(thisQRpair)

if __name__ == '__main__':
    main()