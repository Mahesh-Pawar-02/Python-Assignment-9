# Problem Statement : Write a program which accept two file names from user and compare contents of both the files. If both the 
# files contains same contents then display success otherwise display failure. Accept names of both the files from command line.

import sys

def CompareFiles(File1, File2):
    try:
        F1 =  open(File1, 'r')
        Data1 = F1.read()

        F2 = open(File2, 'r')
        Data2 = F2.read()

        if Data1 == Data2:
            print("Success: Both files contain the same data.")
        else:
            print("Failure: The files contain different data.")

    except FileNotFoundError as eobj:
        print("Error: File does not exist.")
    except Exception as e:
        print("An error occurred: ",eobj)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Assignment9_3.py <file1> <file2>")
    else:
        File1 = sys.argv[1]
        File2 = sys.argv[2]
        CompareFiles(File1, File2)

# How to use the script
# Step 1 : Save the script to a file, for example, Assignment9_4.py.
# Step 2 : Open a terminal or command prompt.
# Step 3 : Navigate to the directory where the script is saved.
# Step 4 : Run the script with the two file names as command line arguments.

# For Example : python Assignment9_4.py file1.txt file2.txt
