#2-misil
class Talaba:
    def __init__(self, fullname, ball):
        self.fullname = fullname
        self.ball = ball
        self.__ball = 0

    def ball_qosh(self, qiymat):
        self.__ball += qiymat

    def info(self):
        print(f"ismi: {self.fullname}")
        print(f"bali: {self.ball}")

t1 = Talaba("Dilnura", "100")
t1.info()


