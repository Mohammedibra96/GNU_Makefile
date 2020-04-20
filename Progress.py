import sys
import re

from progressBar_file import progressBar

import string

#Thsi function shall read the value of the progress 
def ReadProgressValue():
  #open progress.txt 
  f=open('Progress.txt','r')
  text=f.read()
  #get the value of the progress 
  match=re.search(r'(\d+)',text)
  if match:
    result = int(match.group(1))
  return result
 

#This function shall draw the progress 
def drawProgress(MAX_SIZE):

  # Initiates the progessBar
  prog = progressBar(maxValue = int(MAX_SIZE))
  # Uses appendAmount to set current value .
  prog.updateAmount(ReadProgressValue())
  # Draws the progress bar only if it has changed from previous draw() call.
  prog.draw()
  print("")

#this function shall check the validity of the input arguments 

def inputCheck(user_input):
  try:
    val = int(user_input)
    output=1
    if val <= 0:
      print("please chose Number greter than 0, Number = ", val)
    #else:
      #print("Input is an integer number. Number = ", val)
  except ValueError:
    try:
      val = float(user_input)
      print("Input is a float  number. Number = ", val)
    except ValueError:
      print("No.. input is not a number. It's a string")
    output=0
  return output



def main():
  
  if len(sys.argv) == 2:
    
    if inputCheck(sys.argv[1]) == 1:
      drawProgress(sys.argv[1])
    else:
      print("Please chose Number greater than 0")
  else:
    print("Please enter the Max progress value")

main()