class car:
    def __init__(self, color, price, model):
        self.carColor = color
        self.price = price
        self.model = model
        

class cars2:
    name = "Ahmed"
    age = 30

    def myfunc(self):
        print("Hello cars2\n")
        print(self.name)



class cars3:
    
     name = "Mohammed"

     def __init__(self):
         self.callName()
   
     def callName(self):
          print(f"Hello {self.name}")


class car4:
    def __init__(self, color, price, model):
        self.myColor = color
        self.myPrice = price
        self.myModel = model
    
    def myCar(self):
        if self.myModel >= 2018:
           self.myPrice += 5000
           print(f"New model price {self.myPrice}")
        else:
            self.myPrice -= 5000
            print(f"New model price {self.myPrice}")


BMW = car4("Red", 80000, 2018)
Ford = car4("Black", 70000, 2015)

#print(BMW.myColor)
#print(BMW.myPrice)
#print(BMW.myModel)

BMW.myCar()
Ford.myCar()