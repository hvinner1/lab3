import smbus
import time


class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val): #dac fctn application
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

class Joystickclass:

  def __init__(self,address):
    self.PCF8591 = PCF8591(0x48)
   

  def get(self):  
    try:
      self.xval= self.PCF8591.read(0)
      self.yval= self.PCF8591.read(1)
    except Exception as e:
        print ("Error: %s \n" % e)
   




joy = Joystickclass(0x40)


while True:
    joy.get()
    print('{:>3}, {:>3}'.format(joy.xval, joy.yval))
    time.sleep(.1)