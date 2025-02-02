class Card:

    def __init__(self,rank,symbol):
        self.rank = rank
        try: self.value = int(rank)
        except:
            if rank != 'As':
                self.value = 10
            else: self.value = 'As'
        self.symbol = symbol

    def __repr__(self):
        #return f'||{self.rank},{self.symbol},{self.value}||'
        return f'{self.rank} de {self.symbol}'



