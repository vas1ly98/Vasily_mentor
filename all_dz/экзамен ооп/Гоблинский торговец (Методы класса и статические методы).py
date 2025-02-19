class GoblinMerchant:
    def __init__(self, gold):
        self.gold = gold

    @staticmethod
    def tax_rate():
        return  0.1


    @classmethod
    def from_rich_merchant(cls):  # cls ссылается на класс Dog
        return cls(1000)

    def buy_item(self, item_name, item_price):
        total_price = item_price + item_price * self.tax_rate() >= 0
        if self.gold >= total_price:
            self.gold -= total_price
            return (f'Куплен, {item_name}')
        else:
            return "Недостаточно золота!"



merchant = GoblinMerchant(200)
print(merchant.buy_item("Амулет удачи", 150))  # Ожидается успешная покупка или недостаток золота
rich_merchant = GoblinMerchant.from_rich_merchant()
print(rich_merchant.buy_item("Волшебный посох", 500))  # Ожидается успешная покупка
