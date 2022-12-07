import time
from trello_wrapper import *

trello_api_key = "4bdde159796e3cdcf684657fe6263cd6"
trello_token =  "a12115c17037d771f6fb576ea084164f69d0de426fdf55e78d2c7c351aeef1c1"
trello = trello_wrapper(trello_api_key, trello_token)

#Testcase 1 Creating new board
new_board = trello.create_board("Hala_madrid")
print("Created new board",new_board)
time.sleep(3)

#Testcase 2 Creating new card on the board
get_card_id = trello.list_id(new_board)

time.sleep(3)
new_card = trello.create_card2("new_name", get_card_id)
print("Created new card on the board")
print(new_card)
time.sleep(3)

#Testcase 3 Delete the card
del_card = trello.delete_card_action(new_card)
time.sleep(3)
print("Card deleted")

#Testcase 4 Delete Board
time.sleep(10)
trello.delete_board_action(new_board)
print("Board deleted!!!!")
