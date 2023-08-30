import ctypes  #To make basic arrays
from typing import Any  
# Making Python Dynamic List Using C++ Static List
class MeriList:
    def __init__(self):  #Magic Method for Initializing Class
        self.size=1
        self.n = 0
        self.Arr = self.__createArray(self.size)
    def __len__(self):   #Magic Method to find length
        return self.n
    def __getitem__(self,index):  #Magic Method For indexing
        if index>=0 and index<self.n and index%1==0:
            return self.Arr[index]
        else:
            return "IndexError: Invalid Index Value"
    def __str__(self):  #Magic Method for Printing
        res = ""
        for i in range(self.n):
            res+=str(self.Arr[i]) + ","
        return "["+res[:-1]+"]"
    def __delitem__(self,index): #Magic Method to delete an element at a specific location
        if index==self.n-1:
            self.pop()
        if index>=0 and index<self.n and index%1==0:
            ret = self.Arr[index]
            for i in range(index,self.n-1):
                self.Arr[i] = self.Arr[i+1]
            self.n-=1
            return ret
        else:
            return("IndexError: Invalid Index Value")
    def __add__(self,other):  # Magic Method to add two Instances of Class using + operator to create a new instance
        if isinstance(other,MeriList):
            newOne = MeriList()
            for i in range(self.n):
                newOne.append(self.Arr[i])
            for i in range(other.n):
                newOne.append(other.Arr[i])
            return newOne
        elif isinstance(other,list):
            newOne = MeriList()
            for i in range(self.n):
                newOne.append(self.Arr[i])
            for i in other:
                newOne.append(i)
            return newOne
        else:
            return("TypeError: Both Instances must be of same Class")
    def __iter__(self): #Initialising the iterator
        self.itr=0
        return self
    def __next__(self):  #Moving through the iterator
        if self.itr==self.n:
            del self.itr
            raise StopIteration
        ret = self.Arr[self.itr]
        self.itr+=1
        return ret
    def __transfer(self,old,new):  #For Transferring Old Array to New Bigger Array
        for i in range(self.n):
            new[i]=old[i]
        self.Arr = new
        self.size = self.size*2 
    def __createArray(self,size):  # To Create a C Type Static Referrential Array
        return (size*ctypes.py_object)()
    def append(self,e):  #To Append any item at last of list
        if self.n ==self.size:  
            self.__transfer(self.Arr,self.__createArray(self.size*2))
        self.Arr[self.n]=e
        self.n+=1  
    def pop(self):  #To remove item from the last of list
        if self.n!=0:
            self.n=self.n-1
            return self.Arr[self.n]
        else:
            print("EmptyList")
    def clear(self):   #To empty the whole array
        self.Arr=self.__createArray(1)
        self.size=1
        self.n=0
    def index(self,x): #To find the index of given element for the first time in array
        for i in range(self.n):
            if self.Arr[i] == x:
                return i
        return "ValueError: Value not found"
    def insert(self,index,item):  # To insert an element at any specific location in the array
        if index==self.n:
            self.append(item)
            return(item)
        if index>=0 and index<=self.n and index%1==0:
            if self.n ==self.size:  
                newArr = self.__createArray(self.size*2)
                j=0
                for i in range(self.n):
                    if j==index:
                        newArr[j] = item
                        j+=1
                    newArr[j]=self.Arr[i]
                    j+=1
                self.Arr = newArr
                self.size = self.size*2
            else:
                for i in range(self.n,index-1,-1):
                    if i==0:
                        break
                    self.Arr[i]=self.Arr[i-1]
                self.Arr[index] = item
            self.n+=1
            return(item)
        else:
            return("IndexError: Invalid Index Value")
    def remove(self,item): #To remove an specific element
        for i in range(self.n):
            if self.Arr[i]==item:
                self.__delitem__(i)
                return(item)
        return("ValueError: Value not found")