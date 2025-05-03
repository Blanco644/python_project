class Phone:
    def __init__(self,model,brand,cost):
        self.model=model
        self.brand=brand
        self.cost=cost
    def __call(self):
        print('The phone is calling')
    def __play_games(self):
        print('We can play games')
class Camera:
    def __init__(self,type_of_camera,count_mp):
        self.type_of_camera=type_of_camera
        self.count_mp=count_mp
    def photographing(self):
        print('The camera is making photos')
class Smartphone(Phone,Camera):
    def __init__(self, model, brand, cost,type_of_camera,count_mp):
        Phone.__init__(self,model,brand,cost)
        Camera.__init__(self,type_of_camera,count_mp)
    def call(self):
        self._Phone__call()
    def photographing(self):
        print('The Smartphone is making photos')


S1 = Smartphone('poco x7pro','xiaomi','320$','sony350','50')
S1.call()
S1.photographing()