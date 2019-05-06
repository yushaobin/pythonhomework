from pukes.card import Card
import random


def print_cards(cards):
    for card in cards:
        print(card)

class Puke:
    def __init__(self):
        self.colors = ('红桃','黑桃','方片','草花')
        self.values = range(1,14)
        self.init_cards();

    def init_cards(self):
        self.cards = []
        for i in range(0,52):
            index = i // 13
            number = i % 13 + 1
            card = Card(self.colors[index],number)
            self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)


    """
        获取一手牌
    """
    def one_hand_card(self):
        self.shuffle();
        return self.cards[:5]

    """
        判断类型
    """
    def judge(self,handcards):
        isShunzi = False
        isTonghua = False

        colors_set = set()
        value_set = set()
        value_list = []

        for card in handcards:
           colors_set.add(card.color)
           value_set.add(card.value)
           value_list.append(card.value)


        value_list.sort()
        print(value_list)

        if len(handcards) == 1:
            isTonghua = True

        diff = value_list[4] - value_list[0]
        if diff == 4 and len(value_set) == 5:
            isShunzi = True

        if isShunzi and isTonghua:
            return "同花顺"

        if isTonghua:
            return "同花"

        if isShunzi:
            return "顺子"

        if len(value_set) == 5:
            return "杂牌"

        if len(value_set) == 4:
            return "一对"

        card_dict = {}
        for card in handcards:
            data = card_dict.get(card.value)
            if not data:
                data = []
                card_dict[card.value] = data

            data.append(card)


        # 3带1、4带1
        if len(card_dict)  == 2:
            for k , v in card_dict.items():
                if len(v) == 4:
                    return "四带一"

            return "三带一"

        #221,311
        if len(card_dict) == 3:
            for k , v in card_dict.items():
                if len(v) == 3:
                    return "三条"

            return "两对"


p = Puke()
onehand = p.one_hand_card()
print_cards(onehand)
rs = p.judge(onehand)
print(rs)
