# High-level modules should not depend on low-level modules. Both should depend on abstractions.

from abc import ABC, abstractmethod

# Abstract Interface (Abstraction)
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

# Low-level module
class LightBulb(Switchable):
    def turn_on(self):
        print("Light Bulb is on")
        
    def turn_off(self):
        print("Light Bulb is off")

# Another low-level module (New type of bulb)
class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")
    
    def turn_off(self):
        print("Fan is off")

# High-level module
class Switch:
    def __init__(self, device: Switchable):  # Depends on abstraction
        self.device = device
    
    def operate(self, state: str):
        if state == "ON":
            self.device.turn_on()
        elif state == "OFF":
            self.device.turn_off()

# Usage
bulb = LightBulb()
fan = Fan()

switch = Switch(bulb)
switch.operate("ON")  # Output: Light Bulb is on
switch.operate("OFF")  # Output: Light Bulb is off

switch = Switch(fan)
switch.operate("ON")  # Output: Fan is on
switch.operate("OFF")  # Output: Fan is off
