class Car:
    def __init__(self,name,company,color):
        self.name=name
        self.company=company
        self.color=color

    def mufun(self):
        print(" car details:"+self.name,self.company,self.color)

c1=Car("commet","MG","green")
c2=Car("Duster","renault","Red")
c3=Car("Jimny","suzuki","navyblue")
c1.mufun()
c2.mufun()
c3.mufun()
