import random
import os
import sinkei_functions

print("神経衰弱ゲーム！")
print("<初めて作った実用的プログラム in Python>")
card_count = 10
print(f"ここに{card_count}枚のカードがあります")
print("これをめくって、何ターンですべて当てられるか競います")
print("左からn(n ≧ 1)枚目のカードをめくるには、nを入力して下さい")
print("諦めるときは、exitを入力して下さい")

# カードの種類は、1, 2, 3, ... ,card_count/2
cards = sinkei_functions.create_card(card_count)

print("--------")

is_clear = False
turn = 1
clear_cards_count = 0
while not is_clear:
	print(f"{turn}ターン目です")
	sinkei_functions.print_cards(cards)
	mekuru1 = int(input("めくるカード>")) -1
	if(not sinkei_functions.check_card_index(cards,mekuru1)):
		print("正しい数字を入力してください")
		continue
	if cards[mekuru1] < 0:
		print("すでにめくられています")
		continue
	
	os.system("clear")
	
	print(f"めくるカード>{mekuru1+1}")
	sinkei_functions.print_cards(cards,mekuru1)
	mekuru2 = int(input("2枚目にめくるカード>")) -1
	if(not sinkei_functions.check_card_index(cards,mekuru2)):
		print("正しい数字を入力してください")
		continue
	
	if cards[mekuru2] < 0:
		print("すでにめくられています")
		continue
	sinkei_functions.print_cards(cards,mekuru1,mekuru2)
	
	if cards[mekuru1] == cards[mekuru2]:
		print("カードが揃いました！")
		cards[mekuru1] = -cards[mekuru1]
		cards[mekuru2] = -cards[mekuru2]
		clear_cards_count += 2
	print("--------")
	
	if len(cards) == clear_cards_count:
		print("＜ゲームクリア！  おめでとうございます！＞")
		print(f"{turn}ターン目でクリア！")
		print("また遊んでね！")
		break
	turn += 1
