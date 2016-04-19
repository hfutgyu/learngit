class AddBook(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph
        print 'creat instance for:',self.name

    def updatePhone(self,newph):
        self.phone=newph
        print 'update phone for:',self.name

    def updateName(self,newnm):
        self.name=newnm
        print 'new name:',self.name

gyu=AddBook('guang yu','15212775739')
ghb=AddBook('guang hongbao','15212775739')
