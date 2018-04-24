from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class FastLED(ArduinoObject):
    cfg_h_name = 'USE_FastLED'

    def __init__(self, ledType, dataPin, colorOrder, leds, numLEDs, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', ledType, dataPin, colorOrder, leds, numLEDs)

    @arduinoobjectmethod
    def show(self):
        pass

    @arduinoobjectmethod
    def delay(self, delaytime):
        pass

    @arduinoobjectmethod
    def setBrightness(self, brightness):
        pass

    @arduinoobjectmethod
    def setCorrection(self, ledType):
        pass
        