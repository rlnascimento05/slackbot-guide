class SystemStatus:
  def __init__(url, status = '404'):
    self.url = url
    self.status = status
  
  def __str__(self):
    return "Url: %s ; Status: %s ; Erro: %s" % (
            self.url, 
            self.status)