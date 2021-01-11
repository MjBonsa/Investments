from csv import DictReader
import operator

class Investor:

    def __init__(self):
        self.data, self.prices = self.csv_reader()
        #self.data.sort(key=operator.itemgetter("price"))

        #print(max(self.data, key=lambda x: x['price']),
        #       min(self.data, key=lambda x: x['price']))

    def csv_reader(self):
        data = []
        index = 0
        prices = []
        with open('df.csv') as df:
            reader = DictReader(df, delimiter=',')
            for line in reader:
                tmp = {
                    "index":index,
                    "date": line["date"],
                    "time": line["time"],
                    "price": float(line["price"])
                }
                index+=1
                prices.append(float(line["price"]))
                data.append(tmp)
        return data,prices

    #def one_best_transaction(self):
    #    better = {"dateB": 0, "timeB": 0, "dateS": 0, "timeS": 0, "priceB": 0, "priceS": 0, "benefit": 0}
#
    #    for i in range(len(self.data)):
    #        buy = self.data[i]["price"]
    #        for j in range(i, len(self.data), 1):
    #            sell = self.data[j]["price"]
    #            if buy - sell > better["benefit"]:
    #                better = {
    #                    "dateB": self.data[i]["date"],
    #                    "timeB": self.data[i]["time"],
    #                    "dateS": self.data[j]["date"],
    #                    "timeS": self.data[j]["time"],
    #                    "priceB": self.data[i]["price"],
    #                    "priceS": self.data[j]["price"],
    #                    "benefit": buy - sell
    #                }
    #        if i % 50 ==0:
    #            print(i)
    #    print(better)
#
    #def one_best_transaction2(self):
    #    better = {"dateB": 0, "timeB": 0, "dateS": 0, "timeS": 0, "priceB": 0, "priceS": 0, "benefit": 0}
    #    better = 0
    #    for i in range(len(self.data)):
    #        tmp = self.search_max(self.data[i:].copy(),self.data[i]["index"])
    #        if tmp > better:
    #            better  = tmp
    #        if i%100 == 0:
    #            print(i)
    #    print(better)
#
#
    #def search_max(self,data,index):
    #    data.reverse()
    #    tmp = data.pop()
    #    while index > tmp["index"]:
    #        tmp = data.pop()
    #    return tmp["price"]
#
    #def one_best_transaction3(self):
    #    better = {"dateB": 0, "timeB": 0, "dateS": 0, "timeS": 0, "priceB": 0, "priceS": 0, "benefit": 0}
    #    better = 0
    #    for i in range(len(self.data)):
    #        cur = self.data[i]["price"]
    #        maxForCur = max(self.data[(i+2):], key=lambda x: x['price'])
    #        tmp = maxForCur - cur
    #        if maxForCur - cur > better:
    #            better = tmp
    #   print(better)

    def one_best_transaction4(self):
        benefit = 0
        minPrice= self.data[0]["price"]
        for i in range(1,len(self.data),1):
            curBenefit = self.data[i]["price"] - minPrice
            benefit = max(benefit,curBenefit)
            if benefit == curBenefit:
                sell = self.data[i]
            minPrice = min(minPrice,self.data[i]["price"])
            if minPrice == self.data[i]["price"]:
                buy = self.data[i]
        print("Изменение цены акции с момента покупки до момента продажи")
        for _ in range(buy["index"],sell["index"]+1,1):
            print(self.data[_]["date"],self.data[_]["time"],self.data[_]["price"],
                  "\n Стоимость акций в портфеле:",self.data[_]["price"])
        print("Акция была куплена", buy["date"], buy["time"], "за", buy["price"])
        print("Акция была продана", sell["date"], sell["time"], "за", sell["price"])
        print("Выгода составила",benefit)


