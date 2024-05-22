# Problem Statement : Write a program which accept file name from user and open that file and display the contents of that file on screen. 

import os

def main():

    print("Enter the name of file : ", end = " ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File successfully opend in read mode")

        Data = fobj.read()
        print(Data)

        fobj.close()

    else:    
        print("Unable to open as file as file not present in current directory")
        
if __name__ == "__main__":
    main()

# Test Case : 
# Input : Demo.txt 
# Display contents of Demo.txt on console.