# Problem Statement : Write a program which accepts file name from user and check whether that file exists in current directory or not. 

import os

def main():

    print("Enter the name of file : ", end = " ")
    Fname = input()

    if os.path.exists(Fname):
        print("File exists in current directory")

    else:    
        print("File not exists in current directory")
    
if __name__ == "__main__":
    main()

# Test Case : 
# Input : Demo.txt 
# Check whether Demo.txt exists or not. 