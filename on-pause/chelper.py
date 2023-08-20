import os
import glob

#ptype is the files you want for example .c or .out in this case
def get_all_files(type, path):
    return glob.glob("**/*.c", recursive=True)

def compile_c_files(files):

    print("Found files. Try compiling...")

    for file in files:
        print(str(file))
        try:
            os.system("cc " + file + ' -Wall -Wextra -Werror')
        except:
            print("Compiling file {file} failed. Skipping.")


def run(path):

    compile_c_files(get_all_files(path, 'c'))

    out_files = get_all_files(path, 'out')
    if(len(out_files) < 1):
        print("No files found! Check if the file is in the corect folder or if you used the correct absolute path.")
        main()
        return

    for out in out_files:
        os.system(out)
        

def main():
    
    print('\n\n\nC-Helper by Jonas Kauker \n--------------------------')

    choice = int(input("Choose whether you want to use a custom path or the relative path \n1: Relative path (relative means it used the path this file is in currently -> file has to be in the root project folder for example C00) \n2: [NOT WORKIG CURRENTLY] Custom path (type in the absolute path to the folder) \n3: Exit the programm \n=> "))
    
    if(choice == 1):
        print('Relative path: ' + os.path.dirname(__file__))
        run(os.path.dirname(__file__))

    elif(choice == 2):

        #this is goign to be removed once its fixed
        print("Not working for now use the relative function instead")
        main()
        return

        print('Absolute path...')
        absolute = input("Please enter the absolute file pat to the folder: \n")

        if(not os.path.exists(absolute)):
            print("Given path doesnt exist: " + absolute)

        else:
            run(absolute)
            main()
            return
        
    elif(choice == 3):
        print("Exiting programm")
        exit() 

    else:
        print("[ERR] Invalid input provided: " + str(choice))
        main()


main()
