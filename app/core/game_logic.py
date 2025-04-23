# app/core/game_logic.py
import random
from typing import List, Dict
from app.models.game import Card

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = list(range(1, 14))  # 1=Туз, ..., 13=Король

class SolitaireGame:
    """
    Базовая логика игры «Пасьянс Косынка».
    Раздаётся 7 столбцов по возрастанию (1,2,...,7), остальная колода – в stock.
    Карта закрыта (face_up=False), последняя в каждом столбце открыта.
    """
    def __init__(self):
        self.stock: List[Card] = []
        self.waste: List[Card] = []
        # Фундаменты по мастям: карта кладётся, если достоинство на 1 больше
        self.foundations: Dict[str, List[int]] = {suit: [] for suit in suits}
        # 7 столбцов (tableau)
        self.tableau: List[List[Card]] = [[] for _ in range(7)]
        self.init_game()

    def init_game(self):
        # Создаем перемешанную колоду
        deck = [Card(suit=s, rank=r, face_up=False) for s in suits for r in ranks]
        random.shuffle(deck)
        # Раздаём в столбцы
        for i in range(7):
            for j in range(i + 1):
                card = deck.pop()
                card.face_up = (j == i)  # последняя карта в столбце открыта
                self.tableau[i].append(card)
        # Оставшиеся карты в колоду (stock)
        self.stock = deck

    def draw_card(self):
        """
        Берём карту из stock в waste (открывая её). Если stock пуст, перемешиваем waste обратно.
        """
        if self.stock:
            card = self.stock.pop()
            card.face_up = True
            self.waste.append(card)
        else:
            # перемешиваем (карты из waste возвращаются в stock лицом вниз)
            self.stock = [Card(suit=c.suit, rank=c.rank, face_up=False) for c in reversed(self.waste)]
            self.waste.clear()

    def valid_move(self, from_pile: str, to_pile: str) -> bool:
        """
        Проверка валидности хода (необязательна для шаблона).
        В реале здесь проверяется соответствие правил (чёрное-красное, по убыванию/возрастанию).
        """
        # Для упрощения всегда возвращаем True
        return True

    def move_card(self, from_pile: str, to_pile: str, card: Card):
        """
        Переместить карту (или стопку) из одного места в другое.
        from_pile, to_pile могут обозначать: 'waste', 'tableau{index}', 'foundation{Suit}', 'stock'
        """
        # Реализация хода опущена (заглушка)
        pass

    def to_dict(self) -> Dict:
        """
        Конвертирует состояние игры в простой словарь для сериализации (Pydantic сделает остальную работу).
        """
        return {
            "tableau": [[card.dict() for card in col] for col in self.tableau],
            "stock": [card.dict() for card in self.stock],
            "waste": [card.dict() for card in self.waste],
            "foundations": self.foundations
        }
