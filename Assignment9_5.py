# Problem statement : Accept file name and one string from user and return the frequency of that string from file. 

import sys

def CountString(File, Str):
    try:
        File =  open(File, 'r')
        Data = File.read()

        count = Data.count(Str)
        return count

    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception as eobj:
        print(f"An error occurred: ",eobj)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_name> <search_string>")
    else:
        Fname = sys.argv[1]
        String = sys.argv[2]
        
        count = CountString(Fname, String)
        
        print("The string Frequency is : ",count)

if __name__ == "__main__":
    main()

# Test Case : 
# How to use the script
# Step 1 : Save the script to a file, for example, Assignment9_5.py.
# Step 2 : Open a terminal or command prompt.
# Step 3 : Navigate to the directory where the script is saved.
# Step 4 : Run the script with the two file names as command line arguments.

# For Example : python Assignment9_5.py ABC.txt Marvellous