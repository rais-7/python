class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self,other):
        sec1 = self.hour*60*60 + self.minute*60 + self.second
        sec2 =  other.hour*60*60 + other.minute*60 + other.second
        totalSeconds = sec1 + sec2
        finalHour = int(totalSeconds/3600)
        finalMinutes = int((totalSeconds%3600)/60)
        finalSecs = int((totalSeconds%3600)%60)
        return (finalHour, finalMinutes, finalSecs)

time1=(input("enter time1 :" ).split(":"));
time2=(input("enter time2 :" ).split(":"));

t1 = Time(int(time1[0]),int(time1[1]),int(time1[2]))
t2 = Time(int(time2[0]),int(time2[1]),int(time2[2]))
print(t1+t2)

