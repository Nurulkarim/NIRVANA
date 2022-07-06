from datetime import date


def any(m,n=2,*t,**d):
    print(m,n,t,d.get("date"))
any(12,100,2000,999,vacation=20,date= "14 june")