from __future__ import print_function, division

from Card import Hand, Deck

class Hist(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments (or decrements) the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]

class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
        """Computes histograms for suits and hands.
        Creates attributes:
          suits: a histogram of the suits in the hand.
          ranks: a histogram of the ranks.
          sets: a sorted list of the rank sets in the hand.
        """
        self.suit_hist = Hist()
        self.rank_hist = Hist()
        
        for c in self.cards:
            self.suit_hist.count(c.suit)
            self.rank_hist.count(c.rank)

        self.sets = list(self.rank_hist.values())
        self.sets.sort(reverse=True)
 
    def has_highcard(self):
        """Returns True if this hand has a high card."""
        return len(self.cards)

    # # 하나로 모아 버리자 
    # def suit_hist(self):
    #     """Builds a histogram of the suits that appear in the hand.
    #     Stores the result in attribute suits.
    #     """
    #     self.suits = {}
    #     for card in self.cards:
    #         self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    # def rank_hist(self):
    #     self.ranks = {}
    #     for card in self.cards:
    #         self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suit_hist.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        count = 0
        for val in self.rank_hist.values():
            if val == 2:
                count += 1
        if count == 1:
            return True
        return False

    def has_twopair(self):
        count = 0
        for val in self.rank_hist.values():
            if val == 2:
                count += 1
        if count == 2:
            return True
        return False

    def has_triple(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.rank_hist.values():
            if val == 3:
                return True
        return False
     
    def has_straight(self):
        self.key_list = []
        for val in self.rank_hist.keys():
            self.key_list.append(val)
        self.key_list.sort()
        # print(self.key_list)
        if len(self.key_list) < 5:
            # print("cut")
            return False
        for a in range(len(self.key_list) - 5):
            if (self.key_list[a] + 1) == self.key_list[a + 1]:
                # print('in')
                for b in range(a, a + 5):
                    # print(a, self.key_list[b])
                    if (self.key_list[b] + 1) != self.key_list[b + 1]:
                        return False
                return True
        return False

    def has_straightflush(self):
        if self.has_straight and self.has_flush:
            return True
        return False

    def has_threekind(self):
            for val in self.rank_hist.values():
                if val == 4:
                    return True
            return False

    def has_fourkind(self):
        self.make_histograms()
        for val in self.sets:
            if val == 4:
                return True
        return False

    def has_fullhouse(self):
        if self.has_triple() and self.has_pair():
            return True
        return False


    def classify(self):
        self.make_histograms()

        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)

class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(self, num_cards=5, num_hands=10):
        """Deals hands from the deck and returns Hands.
        num_cards: cards per hand
        num_hands: number of hands
        returns: list of Hands
        """
        hands = []
        for i in range(num_hands):        
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands

def main():
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print(total, 'hands dealt:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0: 
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))

        
if __name__ == '__main__':
    main()