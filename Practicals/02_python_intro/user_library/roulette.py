class Roulette:
    def __init__(self, total_money):
        self.remaining_money = total_money
        self.bet_history = []
    
    def roll_roulette(self):
        return random.randint(0,36)
    
    def available_bet(self, bet_amount):
        if self.remaining_money == 0:
            print('You have lost everything. Get lost!')
            return 0
        else:
            return min(self.remaining_money, bet_amount)
    
    def bet_even_odd(self, bet, bet_amount):
        bet_amount = self.available_bet(bet_amount)
        
        num = self.roll_roulette()
        if num == 0:
            num_type = 'zero'
        elif num % 2 == 0:
            num_type = 'odd'
        else:
            num_type = 'even'
        
        if num_type == bet:
            gain = 2 * bet_amount - bet_amount
        else:
            gain = -bet_amount
            
        self.remaining_money += gain
        self.bet_history.append(gain)
        
    def bet_single_number(self, bet, bet_amount):
        bet_amount = self.available_bet(bet_amount)
        
        num = self.roll_roulette()
        if bet == num:
            gain = 35 * bet_amount - bet_amount
        else:
            gain = -bet_amount
            
        self.remaining_money += gain
        self.bet_history.append(gain)    