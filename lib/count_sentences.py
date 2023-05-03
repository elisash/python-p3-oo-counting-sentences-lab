#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self.value
  
  def set_value(self, string):
    if(type(string)== str):
      self.value = string
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self, value):
    if value[-1] == ".":
       return True
    else: 
       return False
  
  def is_question(self, value):
    if value[-1] == "?":
      return True
    else: 
      return False

  def is_exclamation(self):
    return self.value.endswith("!")
  

  
