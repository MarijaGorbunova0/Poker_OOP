"""Simple Poker implementation."""
from collections import Counter

class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        if value not in Hand.values or suit not in Hand.values:
            raise ValueError("you don't have a card")
        self.value = value
        self.suit = suit
       
    def __repr__(self):
        """
        Return a string representation of the card.

        return{value} of {suit}
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"
        


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = []
       

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        if len(self.card) >= 5:
            return False

        for same in self.cards:
            if same.value == card.value and same.suit == card.suit:
                return False
        return True

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards.append(card)
        else:
            return False
       

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        if card in self.cards:
            return True
        else:
            return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards.remove(card)
      
    def get_cards(self):
        """Return a list of cards as objects."""

        return self.cards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        value_index = [Hand.values.index(card.value) for card in self.cards] #получаем индекс карты исходя из всех карт
        value_index.sort()
        return value_index == list(range(value_index[0]), value_index[0]+5) 

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        suits = [card.suit for card in self.cards] #создала список который сохраняет масть карты из всех карт на руках
        return len(set(suits)) == 1

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        return self.is_straight and self.is_flush

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        
        values = [card.value for card in self.cards]
        counts = Counter(values)

        return len(counts) == 2 and 3 in counts.values() and 2 in counts.values()

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        values = [card.value for card in self.cards]
        return any(values.count(value) == 4 for value in values)
      

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        values = [card.value for card in self.cards]
        return any(values.count(value) == 3 for value in values)

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        """
        values = [card.value for card in self.cards]
        return any(values.count(value) == 2 for value in values)