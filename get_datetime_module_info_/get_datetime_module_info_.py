
# TODO : SIMPLE PROJECT TO DISPLAY DATETIME MODULE & IT'S METHODS INFORMATION

from for_datetime_module_ import b as zip_obj

l = ":"*30

def getModuleInfo() :
    '''
    Returns the information about the Datetime module.
    '''
    print(l)
    print("Datetime Module Info : ")
    print(l)
    import datetime 
    print(datetime.__doc__)

def getClassesList():
    '''
    Returns All The Classes defined under Datetime Module.
    '''
    print(l)
    print("Datetime Module Classes :")
    print(l)
    for i,j in enumerate(zip_obj,1) :
        print(i,j[0])

def getClassInfo() :
    '''
    Returns the information about the Specific Class of Datetime module ,
    using the input number given by the user.
    '''
    print(l)
    print("Enter Class Number : ")
    try : 
        cc = input()     
        c = int(cc)
        print(l)
        if c in range(1,9):
            print("Class",zip_obj[c-1][0] , "\n")
            print("Info : \n",zip_obj[c-1][1] , "\n")
            print("-"*50)
            return c
        else :
            print("***Please Enter Number within range***")
    except ValueError:
        print("***Please Enter In Number Format Only***")

#? refer : https://stackoverflow.com/questions/20768856/calling-a-variable-from-one-function-to-another-function-in-python 

def getClassMethodsList() :
    '''
    Returns All the Methods Under specific Class of Datetime Module.
    '''
    getClassesList()
    a = getClassInfo()
    try :         
        print(l)
        print("Methods under Class %s : " %(zip_obj[a-1][0]))
        for i,j in enumerate(zip_obj[a-1][2],1) : 
            print(i,j)
        print(l)
        return a
    except Exception:
        print()

def getClassMethodInfo() :
        '''
        Returns the information about the specific method of any desired class,
        using the input number given by the user.    
        '''        
        try :
            d = getClassMethodsList()
            print(l)
            print("\nEnter the Method Number : ")
            ee = input()
            e = int(ee)
            print(l)
            try :
                if len(zip_obj[d-1][3])+1 > e > 0 :
                    print("="*15,"\n*",zip_obj[d-1][2][e-1],"method : \n")
                    print(zip_obj[d-1][3][e-1])   # returns method info
                else :
                    print('***Please Enter A Positive Number within range***') 
            except  :
                print("***Enter Correct Class Number to Proceed***")

        except ValueError :
            print("\t***Please Enter In Number Format Only***")

def getAll_ClassesMethods_ListsInfo() :  
    '''
    Returns All Classes and Methods Under it along with their information.
    '''
    for i in range(len(zip_obj)):
        print(l)
        print("Class ",zip_obj[i][0],":")
        print("Info :",zip_obj[i][1])
        print(l)
        print("Methods Under Class",zip_obj[i][0],":")
        for e in range(len(zip_obj[i][2])) :
            print("="*15,"\n*",e+1,zip_obj[i][2][e],"method : \n")
            print(zip_obj[i][3][e])     # returns method info
        print(l)
        pass

def run() :
    '''Run'''
    while True :
        print(l)
        print("Get Datetime Module Info")
        print(l)
        a = input(' Enter 1 : Datetime Module Info \
                 \n Enter 2 : Classes Under Datetime Module \
                 \n Enter 3 : Get Class Info \
                 \n Enter 4 : Get Class Methods List \
                 \n Enter 5 : Get Class Method Info \
                 \n Enter 6 : Get All Info \
                 \n Enter 7 : Exit \n ')
        print(l)

        if a == "1" :
            getModuleInfo()

        elif a == "2" :
            getClassesList()

        elif a == "3" :
            getClassInfo()

        elif a == "4" :
            getClassMethodsList()
        
        elif a == "5" :
            getClassMethodInfo()

        elif a == "6" :
            getAll_ClassesMethods_ListsInfo()
            break

        elif a == "7" :
            print("Thank You!")
            print(l)
            break

        elif all(x.isdigit() for x in a) == False :
            print("\n***Please Enter In Number Format***\n")
            print(l)

        else :
            print("\n***Please Enter Number within range***\n")    
            print(l)

if __name__ == '__main__' :
    run()