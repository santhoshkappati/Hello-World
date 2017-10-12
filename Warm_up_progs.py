#### @author Skappati ########

#### Warm up programs of Coding bat puzzeles with solutions ################################################## 
## The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
## We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
## sleep_in(False, False) → True
## sleep_in(True, False) → False
## sleep_in(False, True) → True
################## Exercise-1 @ 12/10/2017 ####################################################################
def sleep_in(weekday, vacation):
  if (not weekday or vacation):
    return True
  else:
    return False

def sleep_in_simplified(weekday,vacation):
  return (not weekday or vacation)
