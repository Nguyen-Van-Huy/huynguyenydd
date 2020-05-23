import sys
import os
def file_read_from_tail(fname,linnes):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize-1
            data = []
            white True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break
file_read_from_tail('D/a.txt',2)
