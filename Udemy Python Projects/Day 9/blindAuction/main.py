from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

while not bidding_finished:
  name = input("What is your name?\n")
  price = input("How much would you like to bid\n")
  bids[name] = price
  should_continue = input("Is there anyone else who would like to bid? Enter Yes or No\n").lower
  if should_continue == "no":
    bidding_finished = True
#   elif should_continue == "yes":
#     clear()
  
# elif nextUp:
# name