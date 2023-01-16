class Time:
    def __init__(self, hour, min, sec):
        self.__hour = hour
        self.__min = min
        self.__sec = sec
    def __add__(self, other):
        __sum1 = (self.__hour*60*60) + (self.__min*60) + (self.__sec)
        __sum2 = (other.__hour*60*60) + (other.__min*60) + (other.__sec)
        return __sum1 + __sum2
h1 = int(input("ENTER HOUR 1: "))
h2 = int(input("ENTER HOUR 2: "))
m1 = int(input("ENTER MINUTE 1: "))
m2 = int(input("ENTER MINUTE 2: "))
s1 = int(input("ENTER SECONDS 1: "))
s2 = int(input("ENTER SECONDS 2: "))
t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)
sum = t1 + t2
hour = int(sum/3600)
min = int((sum % 3600)/60)
sec = int((sum % 3600) % 60)
print("{0} hours: {1} mins: {2} secs".format(hour, min, sec))