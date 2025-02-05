class SmartDevice:
    
    def __init__(self, name):
        '''
        This is the __init__ function. 
        This intializes the status to false.
        This also intializes the name

        Parameters:
        name (string): the name of the smart device
        
        Returns: 
        None 
        '''
        self.name = name
        self.status = False

    def turn_on(self):
        '''
        This function turns on the device by the status to True
      
        Returns: 
        None 
        '''
        self.status = True

    def turn_off(self):
        '''
        This function turns off the device by the status to False
      
        Returns: 
        None 
        '''
        self.status = False
    
    def __str__(self):
        '''
        This function returns the string with name and status

      
        Returns: 
        Name and status (str)
        '''
        if self.status == True:
            return f"{self.name}: ON"
        else:
            return f"{self.name}: OFF"

class Light(SmartDevice):
    
    def __init__(self, name):
        '''
        This is the __init__ function. 
        This intializes the brightness to 100.
        This also intializes the parent function name

        Parameters:
        name (string): the name of the Light
        
        Returns: 
        None 
        '''
        super().__init__(name)
        self.brightness = 100
    
    def adjust_brightness(self, level):
        '''
        This is the adjust_brightness function. 
        If the level is in the range of 1 to 100 inclusive
        the function will make the brightness equal to the level
        Parameters:
        level (int): the level of the Light
        
        Returns: 
        None 
        '''
        if level <= 100 and level >= 1:
            self.brightness = level
    
    def __str__(self):
        '''
        This function returns the string with name and status
      
        Returns: 
        Name and status (str) and Name and Brightness (int) 
        '''
        return f"{super().__str__()}, Brightness: {str(self.brightness)}"
        
class Thermostat(SmartDevice):
    
    def __init__(self, name, temperature = 65.0):
        '''
        This is the __init__ function. 
        This intializes the temperature to 65.
        This also intializes the parent function name

        Parameters:
        name (string), of the thermostat
        
        Returns: 
        None 
        '''
        super().__init__(name)
        self.temperature = temperature

    
    def adjust_temperature(self, temp):
        '''
        This is the adjust_temperature function. 
        This adjust the temperature to the temp the user passed in
        
        Parameters:
        temp (float)
        
        Returns: 
        None 
        '''
        if self._check_temperature_limits(temp) == True:
            self.temperature = temp
    
    def __str__(self):
        '''
        This function returns the string with name and status as well as the temperature.

      
        Returns: 
        Name and status (str) and Temperature (float)
        '''
        return f"{super().__str__()}, Temperature: {str(self.temperature)}"
    
    def _check_temperature_limits(self, temp):
        '''
        Check's the temperature, if temp is greater or equal to 55.0 degrees
        and less than or equal than 80 degrees, 
        
        Parameters: temp (float)
        
        Returns bool — True if the temperature is within the valid range (e.g., between 55°F
        andt 80°F); False otherwise.
        '''
        if temp >= 55.0 and temp <= 80:
            return True
        else:
            return False

class Speaker(SmartDevice):
    def __init__(self, name, volume = 3):
        '''
        This is the __init__ function. 
        This intializes the volume to 3
        This also intializes the parent function name

        Parameters:
        name (string), of the thermostat
        
        Returns: 
        None 
        '''
        super().__init__(name)
        self.volume = volume

    def increase_volume(self):
        '''
        Inputs & Returns: None.
        Description: Increases the volume by 1, with a maximum vol of 10
        '''
        if self.volume < 10:
            self.volume = self.volume + 1
    
    def decrease_volume(self):
        '''
        Inputs & Returns: None.
        Description: Decreases the volume by 1, with a minimum volume of 1.
        '''
        if self.volume > 1:
            self.volume = self.volume - 1

    def __str__(self):
        '''
        Inputs: None.
        Returns: str — A string that includes the device name, its on/off status, and the volume
        setting (e.g., “Outdoor Speaker: OFF, Volume: 5”).
        Description: Returns a string representation of the speaker, 
        showing the name, its current on/off status, and its volume setting
        '''
        return f"{super().__str__()}, Volume: {str(self.volume)}"
    
class SmartHome:
    
    def __init__(self):
        '''
        assigns a blank list to self.devices
        '''
        self.devices = []
    
    def __add__(self, other):
        '''
        Inputs: other (SmartDevice) — An instance of a SmartDevice

        Returns: self
        Description: Overloads the + operator to allow devices
        to be added to the SmartHome instance.
        This method appends the device to the devices list in the SmartHome.
        '''
        self.devices.append(other)
        return self
    
    def turn_off_all(self):
        '''
        Inputs & Returns: None.
        Description: Turns off all devices listed for the smart home instance.
        '''
        for i in self.devices:
            i.turn_off()
    
    def __str__(self):
        '''
        Inputs: None.
        Returns: str — A string representation of the statuses of all devices in the smart home,
        showing the name and current status of each device  
        Description: Returns a string
        listing the name and status of each device in the SmartHome
        instance.
        '''
        return ", ".join(str(device) for device in self.devices)
    

if __name__ == '__main__':

    light = Light('Living room light')
    speaker = Speaker("Bedroom speaker", 5)
    home = SmartHome()
    home.__add__(light)
    home + speaker
    thermostat = Thermostat('home thermo')
    home + thermostat

    print(str(home))