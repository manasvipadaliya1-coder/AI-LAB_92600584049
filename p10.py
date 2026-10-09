print("---------CAREER GUIDANCE SYSTEM------------")
print("answer the following question with yes or no ")

c = input("do you like coding : ")
m= input("do you like mathematics :")
b = input("do you like biology : ")
d = input("do you like drawing : ")

if c=="yes" and m=="yes"and  b=="yes" and d=="yes":
    print("suggested career: biomedical software engineer / medical technlogy specialist")

elif c=="no" and m=="no" and  b=="no" and d=="no":
    print("suggested career: explore your interest and career options further")

elif c=="no" and m=="no" and b=="no" and d=="yes":
    print("suggested career: graphic designer / animator")

elif c=="no" and m=="no" and b=="yes" and d=="no":
    print("suggested career : pharmacist / nurse ")

elif c=="no" and m=="no" and b=="yes" and d=="yes":
    print("suggested career : medical illustrator / healthcare educators")

elif c=="no" and m=="yes" and b=="no" and d=="no":
    print("suggesed career : engineer / data analytics")

elif c=="no" and m=="yes" and b=="no" and d=="yes":
    print("suggested career : architect")

elif c=="no" and m=="yes" and b=="yes" and d=="no":
    print("suggested career : doctor")

elif c=="no" and m=="yes" and b=="yes" and d=="yes":
    print("suggested career : medical illustrator / biological designer")

elif c=="yes" and m=="no" and b=="no" and d=="no":
    print("suggested career : programmer / web developer")

elif c=="yes" and m=="no" and b=="no" and d=="yes":
    print("suggested career : web designer / ui-ux designer ")

elif c=="yes" and m=="no" and b=="yes" and d=="no":
    print("suggested career : health app developer")

elif c=="yes" and m=="no" and b=="yes" and d=="yes":
    print("suggested career : medical illustrator")

elif c=="yes" and m=="yes" and b=="no" and d=="no":
    print("suggested career: software enginer / computer scientist")

elif c=="yes" and m=="yes" and b=="no" and d=="yes":
    print("suggested career : game developer / ui engineer ")

elif c=="yes" and m=="yes" and b=="yes" and d=="no":
    print("suggested career: bioinfrmatics scientist")

else:
    print("try again")

print("thank you for using career guidance system")
