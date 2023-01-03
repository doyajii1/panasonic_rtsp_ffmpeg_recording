#check for file existing and delete
import os
 
class fileOperatorClass:

    def __init__(self):
        pass

    def get_first_added_file(self, path):
        if os.path.exists(path):
            os.chdir(path)
            files = filter(os.path.isfile, os.listdir(path))            
            files = [os.path.join(path, f) for f in files] # add path to each file
            files.sort(key=lambda x: -os.path.getmtime(x))# + is decending(most recent), - is ascending(first added)
            if(len(files) <= 144):
                print("The folder has space")
                return None
            print(files[0])
            return files[0]
        else:
            print("The folder does not exist")
            return None
       
    def delete_file(self, path_w_file_name):
        if os.path.exists(path_w_file_name):
            os.remove(path_w_file_name)
        else:
            print("The file does not exist")

