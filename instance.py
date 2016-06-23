class Item:

    def __init__(self):
        self.clear()

    def clear(self):
        self.janCode = ""
        self.salesPrice = ""
        self.salesPriceNotes = []
        self.shopName = ""
        self.linkUrl = ""
        self.itemName = ""
        self.itemDesc = ""

    def addSalesPriceNotes(self, value):
        self.salesPriceNotes.append(value)

    def getItemInfo(self):
        fields = [("JANコード", self.janCode),
                  ("商品名", self.itemName),
                  ("販売価格", self.salesPrice),
                  ("ショップ名", self.shopName),
                  ("リンクURL", self.linkUrl),
                  ("商品説明", self.itemDesc)]
        for note in self.salesPriceNotes:
            fields.append(("価格備考", note))
        itemInfo = []
        for key, value in fields:
            if not value:
                continue
            itemInfo.append((key, value))
        return itemInfo
