
# TODO : SIMPLE PROJECT TO DISPLAY TIME MODULE & IT'S METHODS INFORMATION

import time 
methods_ = tuple(dir(time))
#? We use tuple type sequence as we have to only access and return the elements of the sequence 

from time import _STRUCT_TM_ITEMS as y
from time import *
methods_info = (y.__doc__, time.__doc__.__doc__, __loader__.__doc__, __name__.__doc__, __package__.__doc__, __spec__.__doc__, altzone.__doc__, 
                asctime.__doc__, ctime.__doc__, daylight.__doc__, get_clock_info.__doc__, gmtime.__doc__, localtime.__doc__, mktime.__doc__, monotonic.__doc__, 
                monotonic_ns.__doc__, perf_counter.__doc__, perf_counter_ns.__doc__, process_time.__doc__, process_time_ns.__doc__, sleep.__doc__, strftime.__doc__, 
                strptime.__doc__, struct_time.__doc__, thread_time.__doc__, thread_time_ns.__doc__, time.__doc__, time_ns.__doc__, timezone.__doc__, tzname.__doc__)

l = "\n" + ":"*30 + "\n"

def getModuleInfo() :
    '''Returns the information about the time module.
& the methods under time module'''
    print(l)
    print("Time Module Info")
    print(l)
    import time as a
    print(a.__doc__)

def getMethodList():
    '''Returns All The Methods defined under Time Module In a Systematic manner'''
    print(l)
    print("Time Methods :")
    print(l)
    for i,j in enumerate(methods_,1) : print(i,j)

def getMethodInfo(c=21) : #* default argument given for the sake of executionTime()
    '''Returns the information about the time module method ,
using the input number given by the user as an argument while calling the function.'''
    print(methods_[c-1] , "method")
    print(methods_info[c-1])
    print("-"*50)

#? OPTIONAL : Using zip() function 
def getMethodInfo_(c=21) :
    '''Same as the getMethodInfo() function ,  difference is we have used zip function to construct a list from zip object of the list : methods_ and methods_info.
In getMethodInfo() function , we directly use the methods of the individual lists'''
    a = zip(methods_ , methods_info)
    b = tuple(a)
    print(b[c-1][0] , "Method")
    print(b[c-1][1])
    print("-"*50)

#*  getMethodInfo_() is advisable to be used due to low execution time than the getMethodInfo() function ,as observed in multiple results

def returnMethodInfo() :
    '''To Return the specific info of a module entered by user  , thus calling getMethodInfo_() function'''
    print(l)
    c = int(input("Enter number : "))
    if c > len(methods_) : 
        raise IndexError("Wrong Input!!!\n\
                        ***Please Enter Number within range***")
    else :
        print(l)
        getMethodInfo_(c)
        # getMethodInfo(c)
        # exectionTime()

def returnAllMethodsInfo():
    g = list(map(lambda a : getMethodInfo(a) , range(1,31)))
    print(g)
            
def exportInfo() :
    '''To  create a file with filename entered by the user 
A file containing info about the Time Module , Time MOdule Methods'''
    import time
    file = input("Enter name for the new text file to be created : ")
    e = time.__doc__
    h = "\n. ".join(dir(time))
    i = "\n" , ":"*50 , "\n"
    with open(f"{file}.txt" , "w") as f :
        f.writelines(i)
        f.write("Time Module")
        f.writelines(i)
        f.write(e)
        f.writelines(i)
        f.write("Time Module Methods : \n")
        f.write(h)
    print("Created File : %s.txt Successfully!"  %(file))

#? OPTIONAL : To test the execution time of the Two methods
def executionTime() :
    ''' To Test the execution time and the time difference between the 2 methods : getMethodInfo & getMethodInfo_
To return the method with least Execution time'''
    from timeit import timeit as a
    x = a(getMethodInfo , number = 10)
    y = a(getMethodInfo_ , number = 10)
    print("without zip function : " , x)
    print("with zip function : " , y)
    print("Least execution time of :")
    print("\t","without zip function" if x < y else "with zip function")

def run() :
    while True :
        print(l)
        print("Get Module Info")
        print(l)
        a = int(input(" Enter 1 : Time Module info \n Enter 2 : Method List \n Enter 3 : Method Info \n Enter 4 : Export All Info To a Text File \n Enter 5 : Execution Time \n Enter 6 : Get All Methods Info \n Enter 7 : Exit \n "))
        print(l)
        if a == 1 : 
            getModuleInfo()

        elif a == 2 : 
            getMethodList()

        elif a == 3 :
            returnMethodInfo()

        elif a == 4 :
            exportInfo()

        elif a == 5 :
            exectionTime()

        elif a == 6 : 
            returnAllMethodsInfo()

        elif a == 7 :
            print("Thank You!")
            print(l)
            break

        else :
            print(" Wrong Input !")
            print(l)
            break
            
run()
