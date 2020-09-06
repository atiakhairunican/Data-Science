#netacad email cth: 'abcd@gmail.com'
email='atiakhairunican@gmail.com'

class titik2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def ambiltitik(self):
        return (self.x, self.y)
    def tambahkan(self, point):
        self.x = self.x + point.x
        self.y = self.y + point.y


def run():
    x,y = input().split()
    x = float(x)
    y = float(y)
    return titik2d(x,y)
