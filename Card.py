class Card:
    def _init_(self,rank,symbol):
        self.rank = rank
        try: self.value = int(rank)
        except:
            if rank != 'As':
                self.value = 10
            else: self.value = 'As'
        self.symbol = symbol



