facebook  = False
twitter   = True
instagram = True

if facebook:
    if instagram:
        print("A person can be a good influencer!")
    elif twitter:
        print("A person can be a good influencer!")
elif twitter:
    if instagram:
        print("A person can be a good influencer!")
else:
    print("A person can't be a good infulencer.")