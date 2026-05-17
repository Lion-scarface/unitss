
class Cm_m:
    def __init__(self,cm):
        self.cm = cm /100
    def intt(self):
        return self.cm
    def strr(self):
        return f"{self.cm} M"
class M_km:
    def __init__(self,m):
        self.m = m /1000
    def intt(self):
        return self.m
    def strr(self):
        return f"{self.m} Km"
class S_min:
    def __init__(self,s):
        self.s = s /60
    def intt(self):
        return self.s
    def strr(self):
        return f"{self.s} min"
class Min_h:
    def __init__(self,min):
        self.min = min // 60
    def intt(self):
        return self.min
    def strr(self):
        return f"{self.min} H"
class H_day:
    def __init__(self,h):
        self.h = h / 24
    def intt(self):
        return self.h
    def strr(self):
        return f"{self.h} day"
class G_kg :
    def __init__(self,g):
        self.g = g / 1000
    def intt(self):
        return self.g
    def strr(self):
        return f"{self.g} Kg"
print(H_day(24).intt()+2)
