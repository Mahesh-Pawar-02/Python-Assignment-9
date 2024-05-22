# Problem Statement : Write a program which accept file name from user and create new file named as Demo.txt and copy all contents 
# from existing file into new file. Accept file name through command line arguments.

import sys

def Dest(SourceFile):
    src = open(SourceFile,"r")
    Data = src.read()

    Dst = open("Demo.txt","w")
    Dst.write(Data)

    print("Data copied to Demo.txt successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment9_3.py <Existing file name>")
    else:
        srcFile = sys.argv[1]
        Dest(srcFile)
    
if __name__ == "__main__":
    main()

# Test Case : 
# Input : ABC.txt 
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 