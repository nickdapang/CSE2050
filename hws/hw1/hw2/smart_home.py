class SmartDevice:
    
    def __init__(self, name):
        self.name = name
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False
    
    def __str__(self):
        if self.status == True:
            return f"{self.name}: ON"
        else:
            return f"{self.name}: OFF"

class Light(SmartDevice):
    
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100
    
    def adjust_brightness(self, level):
        if level <= 100 and level >= 1:
            self.brightness = level
    
    def __str__(self):
        return f"{super().__str__()}, Brightness: {str(self.brightness)}"
        
class Thermostat(SmartDevice):
    
    def __init__(self, name, temperature = 65.0):
        super().__init__(name)
        self.temperature = temperature

    
    def adjust_temperature(self, temp):
        self.temperature = temp
    
    def __str__(self):
        return f"{super().__str__()}, Temperature: {str(self.temperature)}"
    
    def _check_temperature_limits(self, temp):
        if temp >= 55.0 and temp <= 80:
            return True
        else:
            return False

class Speaker(SmartDevice):
    def __init__(self, name, volume = 3):
        super().__init__(name)
        self.volume = volume

    def increase_volume(self):
        if volume < 10:
            volume = volume + 1
    
    def decrease_volume(self):
        if volume > 1:
            volume = volume - 1

    def __str__(self):
        '''returns string and volume'''
        return f"{super().__str__()}, Volume: {str(self.volume)}"
    
class SmartHome:
    
    def __init__(self):
        self.devices = []
    
    def __add__(self, other):
        '''Allow devices to be added to the SmartHome instance'''
        self.devices.append(other)
    
    def turn_off_all(self):
        for i in self.devices:
            i.turn_off()
    
    def __str__(self):
        '''Returns a string of all device status in the SmartHome'''
        return ", ".join(str(device) for device in self.devices)
    

light = Light('Living room light')
speaker = Speaker("Bedroom speaker", 5)
home = SmartHome()
home.__add__(light)
home + speaker

print(str(home))