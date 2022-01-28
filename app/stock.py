class Stock:

    def __init__(self, stock_list:list):

        self.open = stock_list[-1].get("open")
        self.high = stock_list[-1].get("high")
        self.low =  stock_list[-1].get("low")
        self.volume = stock_list[-1].get("volume")

        """Cria duas listas com as datas e os valores
        de close dos ultimos sete dias, a lista é
        invertida para a construção posteriormente
        do gráfico na ordem correta"""

        self.close = [stock.get("close") for stock in stock_list][8::-1]
        self.date = [stock.get("date") for stock in stock_list][8::-1]


    def get_change(self) -> float:
        """Calcula a diferença do valor entre o
        último e penultimo dia de fechamento e retorna
        a porcentagem de variação."""

        day = float(self.close[-1])
        yesterday = float(self.close[-2])

        percent = round((day / yesterday  - 1) * 100,2)
        change = round(yesterday /100 * percent,2)

        results = {
            "percent": percent,
            "change": change
        }

        return results
