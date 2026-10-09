f  = input("fever : (yes/no):")
c = input("cough (yes/no):")
h = input("headache (yes/no):")

if f=="yes" and c=="yes" and h=="yes":
    print("flu or viral infection")
    
elif f=="yes" and c=="no" and h=="no" :
    print("mild infection")
    
elif f=="no" and c=="yes" and h=="no":
    print("throat infection and mild cold")
    
elif f=="no" and c=="no" and h=="yes":
    print("stress,migration and fatigue")
    
elif  f=="yes" and c=="yes" and h=="no":
    print("flu")

elif  f=="yes" and c=="no" and h=="yes":
    print("viral fever")

elif  f=="no" and c=="yes" and h=="yes":
    print("common cold")

elif  f=="no" and c=="no" and h=="no":
    print("healthy")
    
else:
    print("incorrect input")
