import serial
import struct
import time
from ..device import Device


class PM100(Device):
    public = ['power', 'count', 'port']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._port = kwargs.get('com', "USB0::0x1313::0x8072::P2005497::INSTR")
        self.pm = None

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value
        if self.connected:
            self.disconnect()
        try:
            self.connect()
        except:
            pass

    @property
    def power(self):
        if self.pm is None:
            return
        # return self.pm.sense.average
        return self.pm.read

    @property
    def count(self):
        if self.pm is None:
            return
        return self.pm.sense.average.count

    @count.setter
    def count(self, value):
        value = int(value)
        if self.pm is None:
            return
        self.pm.sense.average.count = value

    @property
    def wavelength(self):
        return self.pm.sense.correction.wavelength

    @wavelength.setter
    def wavelength(self, value):
        self.pm.sense.correction.wavelength = value

    @property
    def configuration(self):
        return self.pm.getconfigure

    def connect(self):
        try:
            import visa
            from ThorlabsPM100 import ThorlabsPM100
            rm = visa.ResourceManager()
            inst = rm.open_resource(self._port, timeout=1)
            self.pm = ThorlabsPM100(inst=inst)
        except:
            pass

    @property
    def connected(self):
        if self.pm is not None:
            return True
        return False