import requests

class trello_wrapper:
	def __init__(self,key,token):
		self.query = {
			"key":key,
			"token":token
                }

		self.headers = {
			"Accept": "application/json"
		}
		
		
		self.create_board_url = "https://api.trello.com/1/boards/"
		self.board_id = "https://api.trello.com/1/boards/{}/lists"
		self.create_card = "https://api.trello.com/1/cards"
		self.delete_card = "https://api.trello.com/1/cards/{}"
		self.delete_board = "https://api.trello.com/1/boards/{}"
	def create_board(self,board_name):
		additional_query = {
			"name": board_name
			}
		new_board = requests.request("POST", 
			self.create_board_url, 
			headers = self.headers,
			params = {**self.query, **additional_query}
			)
		data1 = new_board.json()['id'][0:]
		#return new_board.json()
		return data1
	def list_id(self, data1):
	#def list_id(self,new_board):
		idlist = requests.get(
			self.board_id.format(data1),
		headers = self.headers,
		params = self.query
		)
		#idl = [i for i in idlist[0]['id']]		
		#return idlist.json()
		data2 = idlist.json()[0]['id']
		return data2
	def create_card2(self, card_name, data2):

                add_query = {
                "name": card_name,
                "idList": data2
                }

                new_card = requests.request("POST", self.create_card,
                                            params = {**self.query, **add_query}
                                )

                card_id = new_card.json()["id"]
                return card_id

	#def delete_card_action(self, card_id):
		#query = {
		#"id": card_id}
	#	del_card = requests.request("DELETE", self.delete_card.format(card_id), headers=headers, params= self.query)             

#	def delete_board_action(self, data1):
    		#url = "https://api.trello.com/1/boards/{}"
#    #querystring = {"key": key, "token": token}
 #   		response5 = requests.request("DELETE", self.delete_board.format(data1), params= self.query)
	def delete_board_action(self, data1):
    #url = "https://api.trello.com/1/boards/{}"
    #querystring = {"key": key, "token": token}
                response5 = requests.request("DELETE", self.delete_board.format(data1), params= self.query)
 
