import random
class Roulette:
    
    def __init__(self, total_money):
        self.remaining_money = total_money
        self.bet_history = []
    
    def roll_roulette(self):
        return random.randint(0,36)
        #return 10
    
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
            #print(f'Congrats, you won {gain}, the number on roullete was {num_type}')
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
            print(f'You lost. The roullete result was {num} against your {bet}')
            
        self.remaining_money += gain
        self.bet_history.append(gain) 
        #print(f'Your current amount of money: {self.remaining_money}')
    def add_money(self, amount):
        self.remaining_money += amount
        #print(f'You added {amount} to your account')

def gamble_roulette(init_money, strategy, bet_amount = 10):
    gambler = Roulette(init_money)

    bet_amount = bet_amount
    while gambler.remaining_money > 0:
        if strategy == 'odd_even':
            my_bet = 'odd' if random.random() < 0.5 else 'even'
            gambler.bet_even_odd(my_bet, bet_amount)
        elif strategy == 'single_digit':
            my_bet = random.randint(0,36)
            gambler.bet_single_number(my_bet, bet_amount)
    
    return gambler.bet_history