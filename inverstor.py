from csv import DictReader
import operator


class Investor:

    def __init__(self):
        self.data, self.prices = self.csv_reader()
        # self.data.sort(key=operator.itemgetter("price"))

        # print(max(self.data, key=lambda x: x['price']),
        #       min(self.data, key=lambda x: x['price']))

    def csv_reader(self):
        data = []
        index = 0
        prices = []
        with open('df.csv') as df:
            reader = DictReader(df, delimiter=',')
            for line in reader:
                tmp = {
                    "index": index,
                    "date": line["date"],
                    "time": line["time"],
                    "price": float(line["price"])
                }
                index += 1
                prices.append(float(line["price"]))
                data.append(tmp)
        return data, prices


    def one_best_transaction4(self):
        benefit = 0
        minPrice = self.data[0]
        for i in range(1, len(self.data), 1):
            curBenefit = self.data[i]["price"] - minPrice["price"]
            benefit = max(benefit, self.data[i]["price"] - minPrice["price"])
            if benefit == curBenefit:
                sell = self.data[i]
                buy = minPrice
            if self.data[i]["price"] < minPrice["price"]:
                minPrice = self.data[i]

        print("Изменение цены акции с момента покупки до момента продажи")
        for _ in range(buy["index"], sell["index"] + 1, 1):
            print(self.data[_]["date"], self.data[_]["time"], self.data[_]["price"],
                  "\n Стоимость акций в портфеле:", self.data[_]["price"])
        print("Акция была куплена", buy["date"], buy["time"], "за", buy["price"])
        print("Акция была продана", sell["date"], sell["time"], "за", sell["price"])
        print("Выгода составила", benefit)

    

    def lol(self):
        profit = 0
        for i in range(1,len(self.prices),1):
            sub = self.prices[i] - self.prices[i - 1];
            if (sub > 0):
                profit += sub
        print(self.prices)
        print(profit)

    def k_best_transactions(self):
        pass

