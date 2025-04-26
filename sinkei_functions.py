import random

def plain_print(obj):
	print(obj,end="")

def create_card(card_count):
	
	cards = []
	for card_number in range(int(card_count/2)):
		cards.append(card_number+1)
		cards.append(card_number+1)
		
	#　100回くらいかき混ぜたら十分でしょう
	for i in range(100):
		(torikae1,torikae2) = (random.randint(0,len(cards)-1) , random.randint(0,len(cards)-1) )
		w = cards[torikae1]
		cards[torikae1] = cards[torikae2]
		cards[torikae2] = w
		
	return cards

def print_cards(cards,show_card_index = -1,show_card_index2 = -1):
	# cardsの中で-nになってるやつは、nを表示する。いつでも。
	
	#並び替え
	if show_card_index != -1 and show_card_index2 != -1:
		(show_card_index,show_card_index2) = ( min(show_card_index,show_card_index2) , max(show_card_index,show_card_index2) )

	for i in range(len(cards)):
		if i == show_card_index:
			plain_print(f"{cards[show_card_index]} ")
		elif i == show_card_index2:
			plain_print(f"{cards[show_card_index2]} ")
		elif cards[i] < 0:
			plain_print(f"<{-cards[i]}> ")
		else:
			plain_print("* ")
	plain_print("\n")
	
# 大丈夫な数字ならTrue,そうでなければFalse
def check_card_index(cards,index):
	return 0 <= index <= (len(cards)-1)


# 旧バージョンprint_cards

# def print_cards(cards,show_card_index = -1,show_card_index2 = -1):

# 	# 出し方 * * * * ... *
# 	# 出し方 * * 5 * ... *
# 	# 出し方 * * 5 4 ... *
	
# 	if show_card_index == -1 and show_card_index2 == -1 :
# 		# アスタリスク表示
# 		for i in range(len(cards)):
# 			plain_print("* ")
			
# 	elif show_card_index != -1 and show_card_index2 == -1 :
# 		#はじめのアスタリスク
# 		for i in range(show_card_index):
# 			plain_print("* ")
# 		#数字
# 		plain_print(f"{cards[show_card_index]} ")
# 		#最後のアスタリスク
# 		for i in range(len(cards) - (show_card_index + 1)):
# 			plain_print("* ")
			
# 	elif show_card_index != -1 and show_card_index2 != -1:
# 		# まず、index < index2になるようにする
# 		if show_card_index > show_card_index2 :
# 			w = show_card_index
# 			show_card_index = show_card_index2
# 			show_card_index2 = w
			
# 		for i in range(show_card_index):
# 			plain_print("* ")
# 		#数字
# 		plain_print(f"{cards[show_card_index]} ")
		
# 		for i in range(show_card_index2-(show_card_index+1)):
# 			plain_print("* ")
		
# 		plain_print(f"{cards[show_card_index2]} ")
		
# 		for i in range(len(cards) - show_card_index2 -1):
# 			plain_print("* ")
		
# 	plain_print("\n")