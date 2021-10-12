'''x= red, ain1
y=brown, ain2'''


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

  def __init__(self,address,xval,yval):
    self.PCF8591 = PCF8591(address)
    self.xval = 0x40
    self.yval = 0x41

  def get(self):  
    try:
      self.xval= self.PCF8591.read(self)
      self.yval= self.PCF8591.read(self)
    except Exception as e:
        print ("Error: %s \n%s" % e)
    return self.bus.read_byte(self.address)




joy = Joystickclass(0x40)


while True:
    joy.read()
    print('{:>3}, {:>3}'.format(joy.xval, joy.yval))
    time.sleep(.1)