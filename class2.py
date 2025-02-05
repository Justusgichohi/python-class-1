
# class Robot:
#     def self_introduce(self):
#         print("my name is" + self.name)

# r1= Robot()
# r1.name="kyla"
# r1.age=23
# r1.size=43

# r1.self_introduce()

class robot:
    def __init__(self, name, colour, size):
        self.name=name
        self.colour=colour
        self.size=size
    
    def self_introduce(self):
        print("my name is " + self.name)
r1=robot("justus", "red", 23)
r1.self_introduce()

        