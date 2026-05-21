import numpy as np
import torch as torch
import pandas as pd
from google import genai
# class current_dir:
#    def __init__(self):
#       pass
#    def curdir(self):
#       path=pathlib.home()
#       print(path)

# current_dir.curdir()

class datafetch: # gemini api
   def __init__(self):
      self.client = genai.Client(api_key="AIzaSyAvKFYHDspnTt1uADdQWfIOf6_sJT1omMU")
      self.history=[]

   def gemini (self,input):
      while True:
       self.user_input = input
       if self.user_input == "exit": #very important
        break

       self.history.append(f"User: {self.user_input}")

       self.response = self.client.models.generate_content(

        model="gemini-2.5-flash",

        contents=self.history
    )
       self.reply = self.response.text

       self.history.append(f"AI: {self.reply}")

print("2")
    
geminidata=datafetch()
data=geminidata.gemini("how to make bread")
print(data)
