#----------------------Timer-----------------------------#
#This is a timer where you can perform 4 actions:
#1) Start the timer
#2) Stop/Reset the timer
#3) Pause the timer
#4) Resume the timer
'''After pressing key 1 for start
   Any time you press the key 2 it will stop and give the time remaining
   Any time you press the key 3 it will pause
   For continue you have to press key 4 on key board'''
#---------------------------------------------------------#
import msvcrt
import time
a=str
print("            ","Timer","         ")
print(1,"            Start")
print(2,"          Stop/Reset")
print(3,"            Pause")
print(4,"            Resume")
timer=float(input("For how much long you want to keep a timer?\n"))
a=input("What do you want?\n")
while(timer>0):
    timer-=1
    time.sleep(1)
    print(time.gmtime(timer)[3],":",time.gmtime(timer)[4],":",time.gmtime(timer)[5])
    if(msvcrt.kbhit()):
      a=msvcrt.getwch()
      print(a)
      if(a=="2"):
        print("Time remaning ",time.gmtime(timer)[3],":",time.gmtime(timer)[4],":",time.gmtime(timer)[5])
        break
      elif(a=="3"):
          a=msvcrt.getwch()
          while(a!="4"):
            a=msvcrt.getwch()
            if(a!="4"):
              print("Do you want to continue type 4")
      else:
        print("Please try again, there is no command like that")
    if(timer==0):
      print("Time Over")
      break 
















