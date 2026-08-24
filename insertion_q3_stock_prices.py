def insert_price(prices, price):
    a=prices.copy(); a.append(price); i=len(a)-2
    while i>=0 and a[i]>price:
        a[i+1]=a[i]; i-=1
    a[i+1]=price
    return a

if __name__ == "__main__":
    prices=[]
    for p in [102.5,98.3,105.1,100.0,97.8]: prices=insert_price(prices,p)
    assert prices==sorted([102.5,98.3,105.1,100.0,97.8])
    assert prices[0]==min(prices) and prices[-1]==max(prices)
    print("All test cases passed!")
