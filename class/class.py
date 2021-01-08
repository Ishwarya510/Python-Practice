class computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("i5,16gb,1TB",self.cpu,self.ram)
#comp1=computer()
comp1=computer("rey",9) 

comp1.config()      