path0 = 'CREATEnewfile.txt'

if __name__ == '__main__':

    file0 = open(path0, 'r')
    num = int(file0.read())
    file0.close()
    file0 = open(path0, 'w')
    file0.write(str(num+1))
    file0.close()

    # "r"   Opens a file for reading only.
    # "r+"  Opens a file for both reading and writing.
    # "rb"  Opens a file for reading only in binary format.
    # "rb+" Opens a file for both reading and writing in binary format.
    # "w"   Opens a file for writing only.
    # "a"   Open for writing.The file is created if it does not exist.
    # "a+"  Open for reading and writing.The file is created if it
    #       does not exist.

    file1 = open('example{}.py'.format(num+1), 'w')
    file1.close()