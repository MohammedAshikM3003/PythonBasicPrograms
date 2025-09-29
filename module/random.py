import random

def otp():
    return(random.randint(1000,9999))



def cotp():
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    u=random.choice(l)
    k=random.choice(l)
    return(u+str(otp())+k+str(otp()))

print(cotp())


print(random.uniform(1,2))