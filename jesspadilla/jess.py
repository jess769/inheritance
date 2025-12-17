
class Vehicle:
    def start(self):
        print("The vehicle starts.")

class Car(Vehicle):
    def drive(self):
        print("The car is driving.")

print("SINGLE INHERITANCE")
c = Car()
c.start()
c.drive()
print()


class Teacher:
    def teach(self):
        print("I can teach.")

class Researcher:
    def research(self):
        print("I can do research.")

class Professor(Teacher, Researcher):
    def role(self):
        print("I am a professor.")

print("MULTIPLE INHERITANCE")
p = Professor()
p.teach()
p.research()
p.role()
print()


class Appliance:
    def power_on(self):
        print("The appliance is powered on.")

class WashingMachine(Appliance):
    def wash(self):
        print("Washing clothes.")

class SmartWasher(WashingMachine):
    def wifi_control(self):
        print("Controlled using WiFi.")

print("MULTILEVEL INHERITANCE")
sw = SmartWasher()
sw.power_on()
sw.wash()
sw.wifi_control()
print()


class Bird:
    def fly(self):
        print("The bird can fly.")

class Eagle(Bird):
    def hunt(self):
        print("The eagle hunts.")

class Sparrow(Bird):
    def chirp(self):
        print("The sparrow chirps.")

print("HIERARCHICAL INHERITANCE")
eagle = Eagle()
sparrow = Sparrow()
eagle.fly()
eagle.hunt()
sparrow.fly()
sparrow.chirp()
print()

class Gadget:
    def __init__(self, name):
        self.name = name

    def gadget_info(self):
        print("Gadget name:", self.name)

class Tablet(Gadget):
    def draw(self):
        print("This gadget can be used for drawing.")

class Speaker:
    def play_music(self):
        print("This gadget can play music.")

class SmartTablet(Tablet, Speaker):
    def browse(self):
        print("This gadget can browse the internet.")

print("HYBRID INHERITANCE")
st = SmartTablet("iPad")
st.gadget_info()
st.draw()
st.play_music()
st.browse()