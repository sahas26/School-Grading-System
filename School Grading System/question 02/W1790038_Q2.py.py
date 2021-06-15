#question 02
#D.C.Sahas Kulasekera
#IIT ID- 20191223
#21.03.2020
progress_count = 0
trailing_count = 0
exclude_count = 0
retriever_count =0

while True:

    try:
        PassCredits =int(input("please enter your pass credits here:"))
        DeferCredits =int(input("please enter your Defer Credits credits here:"))
        FailCredits =int(input("please enter your Fail Credits credits here:"))
    except ValueError:
        print("integer required")

    Total=PassCredits+DeferCredits+FailCredits
    if (PassCredits in range(0,121,20) and DeferCredits in range(0,121,20) and FailCredits in range(0,121,20)):
        if Total==120:
             if PassCredits==120:
                 progress_count = progress_count + 1
                 print("progress")
                 
             elif PassCredits==100:
                 trailing_count = trailing_count + 1
                 print("progress-module trailer")
                 
             elif FailCredits>60:
                 exclude_count = exclude_count + 1
                 print("Exclude")
                 
             else:
                 retriever_count = retriever_count + 1
                 print("do not progress-module retraiver")
        else:
            print("Total incorrect")

        if (input( "enter ‘q’ to quit or press Enter to continue.. : ") == "q"):
            print("Progress ",progress_count," : ",end='')
            for i in range (0,progress_count):
                print("*",end='')
            print("\n",end='')

            print("Trailing ",trailing_count," : ",end='')
            for i in range (0,trailing_count):
                print("*",end='')
            print("\n",end='')

            print("Retriever ",retriever_count," : ",end='')
            for i in range (0,retriever_count):
                print("*",end='')
            print("\n",end='')

            print("Excluded ",exclude_count," : ",end='')
            for i in range (0,exclude_count):
                print("*",end='')
            print("\n")

            print(progress_count+trailing_count+retriever_count+exclude_count , " outcomes in total.")
            break;
    else:
        print("Range Error")
