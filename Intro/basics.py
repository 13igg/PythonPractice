import operator

#Using the format function
name = "Julie"
age = "42"

sentence = "Hi my name is {} and I am {} years old".format(name,age)
print(sentence)

#manipulation
first100Characters = sentence[:100] 

#

#If else statement
year = 1830
if year < 2100 and year > 2000:
    print("Welcome to the 21st century!")
else:
    print("You are before or after the 21st century")
#

#functions
def trippleprint(s):
    print(s+s+s)
#

#lists
shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]
#

#loops
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for num in numbers:
    if(num > 90):
        print(num)
#

#dictionary
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = dict(zip(words, definitions))
print(cooldictionary)
#

#Class
#Something weird is classes can have extra variables that do not exist in the actual definition. So we could say
#car c = Car(2018, "chevy", "cobalt")
#c.tireCondition = new;
class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def age(self):
        return 2018 - self.year
#

#Helper Functions
#length
stringTest = "ThisIsAtest"
len(stringTest) #12

#split
stringTest2 = "This Is A Sentence" #
string2Words = stringTest2.split() #[This, Is, A, Test]
string2Length = len(string2Words) #4

#sorting
#What is operator? You need to 'import operator' at the top of the app
testDict = {}
sorted(testDict.items(), key = operator.itemgetter(1), reverse=True)


#