import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init(storedValue = 12)

  @sp.entry_point
  def divide(self, params):
    sp.verify(params.divisor > 5)
    self.data.storedValue //= params.divisor

  @sp.entry_point
  def double(self):
    self.data.storedValue *= 2

  @sp.entry_point
  def replace(self, params):
    self.data.storedValue = params.value