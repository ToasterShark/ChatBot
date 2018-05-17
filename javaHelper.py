import math
import numpy
import re
import urllib2 as url

ATTENTIONSPAN = 5


def main():
    print "----------------\nHi! \n\nI'm here to help you with any \nJava related problems you may have. \n\nJust ask me a question and I'll try to help\n----------------\n\n"
    file = open("classList.txt","r")
    classList = file.read()
    file = open("mycl.txt","r")
    mycl = file.read()

    count = 0
    while count < ATTENTIONSPAN:
        ask(count)
        getResponse(classList,mycl)
        count+=1
    print "       zz  zz  zz zz\n      /  zz  zz  zz\n(- .-)"

def ask(count):
    if count == 0:
        print "\nHello, how can I help?\nvvvvv"
    elif count < ATTENTIONSPAN-(4*ATTENTIONSPAN/5):
        print "\nHello again, another question?\nvvvvvv"
    elif count < ATTENTIONSPAN-(3*ATTENTIONSPAN/5):
        print "\n...Yeah... Just ask a question I guess\nvvvvvv"
    elif count < ATTENTIONSPAN-(2*ATTENTIONSPAN/5):
        print "\nYou know... there is a thing called google right?\nv vv v"
    elif count < ATTENTIONSPAN-(ATTENTIONSPAN/5):
        print "Pleaaaase, leave me alone already\nv"
    elif count < ATTENTIONSPAN:
        print "Stop. Asking. Questions."

def getResponse(cl,mycl):
    inp = raw_input("\n:")

    answer(interpret(inp,cl,mycl))

def interpret(inp,cl,mycl):
    inp = re.split("[@0123456789\-\+\_\=(,;:\.?! )\\\*/\'\"\\n]+",inp)
    cll = cl.lower()
    mycll = mycl.lower()
    for word in inp: #goes through each word
        print "word" + str(word)

        ind = mycll.find(word.lower()) #checks if they are in the preloaded stuff
        if ind >= 0 and mycll[ind-1] ==" ":
            en = ind
            for i in range(ind,len(mycll)):
                if mycll[i]==" ":
                    en = i

                    print "en:" + str(en)
                    print "ind:" + str(ind)
                    return mycll[ind:en]

    for word in inp:
        ind = cll.find(word.lower()) #if not preloaded, go to the backup
        while cll[ind-1] is not " ":
            ind-=1
        if ind>=0:
            en = ind
            for i in range(ind,len(cll)):
                if cll[i]==" ":
                    en = i-1
                    break
            print "en:" + str(en)
            print "ind:"+str(ind)
            return cl[ind:en]


def answer(keyword):
    print "\n----------------"
    if keyword is None:
        print "I have no clue what that means, B A K A"
        print "----------------\n"
        return
    if keyword == "rectangle":
        print "A Rectangle is an object that is made up of four sides, and is defined by the X and Y coordinates of the the top left corner, and the dimensions in width(X length) and height(Y length)"
        print "Rectangles are constructed as such: Rectangle myrectangle = new Rectangle(x,y,w,h);"
        print "There are methods to transform and analyze Rectangles"
        print "----------------\n"
        return
    elif keyword == "array":
        print "An Array is a list of a fixed size comprised of a certain object type - you cannot make an int array and put a string into it"
        print "Constructor: ObjectType[] myarray = ObjectType[size]"
        print "There are manipulation methods and analytical methods for Arrays"
        print "----------------\n"
        return
    elif keyword == "arrayList":
        print "Similar to an array, except there is not a fixed size - size can be set, but it is variable"
        print "Constructor: Arraylist<ObjectType> myarraylist = new ArrayList<ObjecetType>()"
        print "Can add info at certain indeceses"
        print "----------------\n"
        return
    elif keyword == "string":
        print "Concatenation of characters, denoted by double quotation marks"
        print "Constructor: String mystring = \"example text\""
        print "Many many many many many different ways to manipulate and analyze"
        print "----------------\n"
        return
    elif keyword == "integer":
        print "Number with no decimal points"
        print "Constructor: int myint = 10"
        print "If a number with decimals is entered, the decimals will simply be cut off, NOT ROUNDED"
        print "Good for counting, easy to manipulate"
        print "----------------\n"
        return
    elif keyword == "double":
        print "Like an int, only with decimal places this time"
        print "Constructor: Double mydouble = 10.09"
        print "----------------\n"
        return
    elif keyword == "long":
        print "like double, but longer"
        print "Constructor: long mylong = 10.0000000000000009"
        print "----------------\n"
        return
    elif keyword == "boolean":
        print "Either set to TRUE (1) or FALSE (0), and can be switch between the two"
        print "Constructor: Boolean myboolean = TRUE"
        print "Just a yes or no, use to switch between states or something."
        print "----------------\n"
        return
    elif keyword == "parse":
        print "Parsing is to extrapolate a certain data type from another: to parse a string from an int is to take the int 1 and turn it into the string \"1\""
        print "Can either be done from/to a string, or between any of the number datatypes"
        print "Use: String mystring = \"number 15 is good\";\nint myint = Integer.parseInt(mystring)"
        print "----------------\n"
        return


    #print "https://docs.oracle.com/javase/7/docs/api/java/util/" + keyword + ".html"

    #page = url.urlopen("https://docs.oracle.com/javase/7/docs/api/java/util/" + keyword + ".html").read()
    print "this is what I would do:\n   go to this link and do what they say: https://docs.oracle.com/javase/7/docs/api/java/util/" + keyword + ".html"
    #print page
    print "----------------\n"

if __name__ == '__main__':
    main()

     

