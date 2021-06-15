#question 01
#D.C.Sahas Kulasekera
#IIT ID- 20191223
#19.03.2020
try:
    PassCredits =int(input("please enter your pass credits here:"))
    DeferCredits =int(input("please enter your DeferCredits credits here:"))
    FailCredits =int(input("please enter your FailCredits credits here:"))
except ValueError:
    print("integer required")

Total=PassCredits+DeferCredits+FailCredits
if (PassCredits in range(0,121,20) and DeferCredits in range(0,121,20) and FailCredits in range(0,121,20)):
    if Total==120:
         if PassCredits==120:
             print("progress")
         elif PassCredits+DeferCredits==100:
             print("progress-module trailer")
         elif FailCredits>60:
             print("Exclude")

         else:
             print("do not progress-module retraiver")
    else:
        print("Total incorrect")
else:
    print("Range Error")
