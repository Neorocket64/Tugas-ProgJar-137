import shelve
import uuid
import os
import io


class File:
    def Upload(self,nama=None,data=None):
        f=open("server/"+nama, "wb")
        f.write(data)
        f.close()
        return True
    def Download(self,nama=None):
        if os.path.isfile("server/"+nama):
            myfile = open("server/"+nama, "rb")
            data=myfile.read()
            myfile.close()
        else:
            data=b'File not Exist'
        return data
    def List(self):
        list = os.listdir("server")
        f = []
        for filename in list:
            f.append(filename)
        return f

# if __name__=='__main__':
#     p = File()
#     # data=open("client/logo.gif", 'rb')
#     # p.Upload("logo.gif",data.read())
#     # print(p.List())
#     print(p.Download("test1.txt"))
