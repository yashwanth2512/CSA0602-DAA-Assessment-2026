def pick_up_card(hand, card):
    a = hand.copy(); a.append(card); i = len(a)-2
    while i >= 0 and a[i] > card:
        a[i+1] = a[i]; i -= 1
    a[i+1] = card
    return a

if __name__ == "__main__":
    hand=[]
    for card in [7,2,9,4,1]: hand=pick_up_card(hand,card)
    assert hand == sorted([7,2,9,4,1]) and pick_up_card([],5)==[5]
    print("All test cases passed!")
