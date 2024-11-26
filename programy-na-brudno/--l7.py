class Rocket():
    def init(self, Name,x=0,y=0):
             self.x=x
             self.y=y
             self.Name=Name
    def move(self,x,y):
        self.x=x
        self.y=y
    def get_position(self,x,y):
        return '-aktualna pozycja-'

    def get_distance(self, ):
        return '-dystans między rakietami-'
    def __str__():
        return Name, '-pozycja-'
    
rakieta= Rocket()
rakieta.Name='A'
print(rakieta)
