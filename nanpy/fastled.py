from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class FastLED(ArduinoObject):
    cfg_h_name = 'USE_FastLED'

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

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

    class addLeds:
        def __init__(self, ledType, dataPin, colorOrder):
            self._LED_TYPE = ledType
            self._DATA_PIN = dataPin
            self._COLOR_ORDER = colorOrder
            
    @arduinoobjectmethod
    def customAddLeds(self, addLeds, ledType, dataPin, colorOrder, leds, numLEDs):
        return addLeds<ledType,dataPin,colorOrder>(leds, numLEDs)
        