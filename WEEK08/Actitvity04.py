# Parent class
class Device:
    def power_on(self):
        print("Device is now powered on.")

# Child class inheriting from Device
class Smartphone(Device):
    def launch_app(self, app_name):
        print(f"Launching {app_name} on smartphone...")

# Creating an instance of Smartphone
my_phone = Smartphone()

# Calling method from parent class
my_phone.power_on()

# Calling method from child class
my_phone.launch_app("Camera")