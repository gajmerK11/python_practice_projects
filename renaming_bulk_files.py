# we use 'os' library to get our os - it allows us to interact with our file system
import os

# function to rename multiple files
def main():
    i = 0
    # give the path of files which you want to rename
    path = "C:/Users/asus/Downloads/test/"
    # for loop to loop through all the files
    for filename in os.listdir(path):
        # format of the name that we want to rename as 'picture0.png'
        my_dest = "picture" + str(i) + ".png"
        my_source = path + filename
        my_dest = path + my_dest

        '''
        we have created my_source and my_dest because:
        the function 'os.rename(old_name, new_name)' expects either:
        just the file name (if it's in the same folder as your python script), or
        the full path to the file (if it's in a different folder)
        since this python script and files to be renamed are in different folders, we have created full paths for the 'old_name' and stored in my_source and for 'new_name' stored in my_dest like below:

        os.rename("C:/Users/asus/Downloads/test/photo1.jpg","C:/Users/asus/Downloads/test/picture0.png")
        above equals to:
        os.rename(my_source, my_dest)
        
        '''
        os.rename(my_source, my_dest)
        i += 1

# what this does is when we run this program it immediateley calls the main() function
if __name__ == '__main__':
    main()