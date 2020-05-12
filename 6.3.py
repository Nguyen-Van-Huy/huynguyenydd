class nguoi(object):
    def getgender(self):
        return "Unknown"
class nam(nguoi):
    def getgender(self):
        return "nam"
class nu(nguoi):
    def getgender(self):
        return "nu"
anam=nam()
anu=nu()
print (anam.getgender())
print (anu.getgender())
    
