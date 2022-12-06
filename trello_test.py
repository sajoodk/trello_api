import time
from trello_wrapper import *

trello_api_key = "4bdde159796e3cdcf684657fe6263cd6"
trello_token =  "a12115c17037d771f6fb576ea084164f69d0de426fdf55e78d2c7c351aeef1c1"
trello = trello_wrapper(trello_api_key, trello_token)

new_board = trello.create_board("real_board")
print(new_board)
get_card_id = trello.list_id(new_board)

print(type(get_card_id))

new_card = trello.create_card2("new_name", get_card_id)

print(new_card)
time.sleep(3)
del_card = trello.delete_card(new_card)

#trello.delete_board(new_board)
