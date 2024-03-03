from replit import clear
from art import logo

print(logo)

auction = {}
highest_price = 0
winner_name = ""
auction_live = True

while auction_live:
  name = input("What is your name?\n")
  bid = int(input("What is your bid price?\n"))
  auction[name] = bid
  if input("Are there any other bidders?\n").lower() == "no":
    auction_live = False
  clear()

for key in auction:
  if auction[key] > highest_price:
    highest_price = auction[key]
    winner_name = key


print(f"The winner is {winner_name} with a bid of ${highest_price}")