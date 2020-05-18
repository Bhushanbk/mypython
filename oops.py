class student:
    def get_details(self):
        self.name="john"
        self.rno=420
        self.fee=50000.0
    def put_details(self):
        print("name=",self.name)
        print("rno=",self.rno)
        print("fee=",self.fee)
s=student()
s.get_details()
s.put_details()
        