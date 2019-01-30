class FeederStatus:
  def __init__(self, origin, interface, status = 'missing', error = 'missing'):
    self.origin = origin
    self.interface = interface
    self.status = status
    self.error = error
  
  def __str__(self):
    return "Origem:%s ; Interface: %s ; Status: %s ; Erro: %s" % (self.origin, 
            self.interface, 
            self.status, 
            self.error)