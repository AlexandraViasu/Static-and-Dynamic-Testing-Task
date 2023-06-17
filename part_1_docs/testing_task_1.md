### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  #the function that defines this class is missing

  def check_for_ace(self, card):
    #there is only one equal sign below (there should be 2 equal signs, or another sign to accompany the equal sign)
    if card.value = 1:
      return True
    #there should be a colon after else
    else
      return False
   
  #1. def is wrongly spelled as 'dif' 
  #2. there is no comma between card1 and card2
  dif highest_card(self, card1 card2):
  #indendation error - if should be indented
  if card1.value > card2.value:
    #card is not defined
    return card
  else:
    return card2
  

#indentation error - self is not accessed by pylance because all def functions should be alligned for the CardGame class
def cards_total(self, cards):
  #total is not given a value
  total
  for card in cards:
    total += card.value
    #return indentation is not correct, should be outside the for loop
    #TypeError: can only concatenate str (not "int") to str
    return "You have a total of" + total
  
```
