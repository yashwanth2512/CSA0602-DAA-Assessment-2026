def insert_updated_score(board, score):
    a = board.copy(); shifts = 0; i = len(a)-1
    a.append(score)
    while i >= 0 and a[i] < score:
        a[i+1] = a[i]; shifts += 1; i -= 1
    a[i+1] = score
    return a, shifts

if __name__ == "__main__":
    board=[980,875,760,690,500]
    assert insert_updated_score(board,820)[0] == [980,875,820,760,690,500]
    b,s=insert_updated_score(board,100); assert b[-1]==100 and s==0
    print("All test cases passed!")
