import sys
sys.stdin = open('input.txt')

def get_card(list_a):
    number_paper = [0] * 10
    for num in list_a:
        number_paper[num] += 1
    paper_number = number_paper[0]
    card_list = []
    for i in range(len(number_paper)):
        if paper_number <= number_paper[i]:
            paper_number = number_paper[i]
            card_list.append(i)

    return card_list[len(card_list)-1], paper_number


T = int(input())
for i in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    print(f'#{i}', get_card(cards)[0], get_card(cards)[1])


