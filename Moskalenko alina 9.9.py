
T = int(input())
for _ in range(T):
    V = int(input())
    votes = {}

    for _ in range(V):
        vote = int(input())
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    max_vote_count = -1
    best_number = -1
    for num, count in votes.items():
        if count > max_vote_count or (count == max_vote_count and num < best_number):
            max_vote_count = count
            best_number = num

    print(best_number)