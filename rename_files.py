import os
def rename_files():
    # get file names from a folder
    files_list = os.listdir("path tot folder ")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("path to chage dir")
    #for each file rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(saved_path)
rename_files()
