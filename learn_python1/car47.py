class car:
    def __init__ (self,model,year,color,for_sale):             # constructor
        self.model = model
        self.year = year                                       # these are attribute
        self.color = color
        self.for_sale = for_sale
# method = action that a object can perform
# function that belong to object
    def drive(self):
        print("you drive the car")
    def stop(self):
        print("you stop the car")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")