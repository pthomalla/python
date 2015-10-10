import re
import timeit
import string

def capwords(string):
    def repl_func(m):
        return  m.group(1).upper() + m.group(2) 
    return re.sub("(\w)(\S*)", repl_func, string)                                         

text = ("however, deadlines don't have to lead to complexity.\tinstead of saying\n"
        "    \"this deadline prevents me from writing simple code\"\none could equally say,\n"
        "    \"i am not a fast-enough programmer to make this simple.\" 1go ")

def test():
    capwords(text)
def test2():
    text.title();
def test3():
    string.capwords(text)

print( capwords(text) )
print("time regular expression:\t", timeit.timeit(test,  number=10000),"\n\n")
print( text.title() )
print("time of title:\t\t\t",       timeit.timeit(test2, number=10000),"\n\n")
print( string.capwords(text) )
print("time of string.capwords:\t", timeit.timeit(test3, number=10000))
