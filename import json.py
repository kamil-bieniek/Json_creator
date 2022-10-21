import json

def cleaning(filename):
    x = ""
    clean = input("Do you want clean our json list ?: Y/N").upper()
    if(clean == "Y"):
        with open(filename, "w") as f:
            f.write(x)
            
class people:

    def __init__(self, name, surname, age, weigth, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weigth = weigth
        self.height = height
        self.Bmi = int(weigth / ((height/100)**2))

    def __str__(self):
        return "enter your data, we will count your BMI and add you to the list"

    def BMI(self):
       print("Your BMI is : ", self.Bmi)

    def Json_creator(self, filename):
        myDict = {"name": self.name,
                  "surname": self.surname,
                  "age": self.age,
                  "weigth": self.weigth,
                  "height": self.height,
                  "BMI ": self.Bmi,
                  }
        with open(filename, "a") as f:
            f.write(json.dumps(myDict, indent=2))

cleaning("Json_creator.json")
while(True):
    counter = int(input("how many people do you want to enroll?"))
    for x in range(counter):
        name = input("tell me your name : ")
        surname = input("tell me your surname : ")
        age = int(input("give me age : "))
        weigth = int(input("weight :"))
        height = int(input("height :"))

        p1 = people(name, surname, age, weigth, height)
        p1.BMI()
        p1.Json_creator("Json_creator.json")
    break
