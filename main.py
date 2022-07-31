import qrcode

class code:
  
  def __init__(self,dado):
    self.info = dado
    self.info = qrcode.make(dado)
    self.info.save("qr_novo.png")

a = code("paralelepido")
