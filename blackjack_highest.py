# Input: ["four","ace","ten"]
# Output: below ten

# Input: ["ace","queen"]
# Output: blackjack ace


cards = {"ace":1, "two":2, "three":3, "four":4, "five":5, "six":6,
        "seven":7, "eight":8, "nine":9, "ten":10, "jack":10, 
        "queen":10, "king":10}
highest_card = {"king", "queen", "jack", "ten", "nine", "eight",
                "seven", "six", "five", "four", "three", "two"}
def black_jack_highest(strArr):
  total = sum([cards[card] for card in strArr])
  if total < 12 and "ace" in strArr:
    total += 10
  highest_card = pick_highest_card(strArr,total)
  if total > 21:
    return f"above {highest_card}"
  if total < 21:
    return f"below {highest_card}"
  return f"blackjack {highest_card}"

def pick_highest_card(strArr,total):
  if total == 21 and "ace" in strArr and len(strArr) == 2:
    return "ace"

  return list(filter(lambda x:x in strArr, highest_card))[0]

 # keep this function call here 
print(black_jack_highest(input()))