# Develop a banking application from scratch. 
# 1st tier: record and hold transactions (deposits and transfers). 
# 2nd tier: do data metrics, returning the top k accounts with outgoing money 
# 3rd tier: add scheduled transactions and canceling them
# 4th tier: merge two accounts while maintaining separate account histories
from dataclasses import dataclass 
from  datetime import datetime, timedelta
from collections import defaultdict
from time import sleep

# improvements
# rename s->from, t->to
@dataclass
class Tx:
    type: str
    s: int | None
    r: int | None
    ts: datetime
    amount: int
    original_account: int | None = None

class Bank:
    def __init__(self, balances: list[int]):
        self._validate_balances(balances)
        self._balances = balances
        self.transactions : list[Tx] = []
        self.scheduled_transactions : list[Tx] = [] 

    def _validate_balances(self,balances):
        if not isinstance(balances,list):
            raise ValueError('Needs to be a list')
        if not all([isinstance(cur_v, int) for cur_v in balances]):
            raise ValueError("Values need to be int")
    
    def _validate_account(self,account_number):
        if account_number < 0 or account_number > len(self.balances):
            raise ValueError("Account idx must be int")
    
    def _validate_money(self, money):
        if isinstance(money, (int, float)): 
            if money < 0:
                raise ValueError("must be higher than 0")
            else:
                return money
        elif isinstance(money,str):
            try:
                money = int(money)
                if money < 0:
                    raise ValueError("must be higher than 0")
                else:
                    return money
            except ValueError:
                raise ValueError("must be higher than 0")
        else:
            raise ValueError("must be higher than 0")
        
    @property
    def balances(self):
        return self._balances

    @balances.setter
    def balances(self, value):
        if type(value) != list[int]:
            raise ValueError("Needs to be an array of integers")
        self._balances = value
    
    @balances.getter
    def balances(self):
        return self._balances
        
    def deposit(self, account: int, money: int) -> bool:
        self._validate_account(account)
        validated_money = self._validate_money(money)
        self.balances[account] += validated_money
        tx = Tx('deposit', s=None, r=account, ts=datetime.now(), amount=money)
        self.transactions.append(tx)
                    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        money = self._validate_money(money)
        self._validate_account(account1), self._validate_account(account2)
        if money < self.balances[account1]:
            self.balances[account1]-=money
            self.balances[account2]+=money
            tx = Tx('transfer', s=account1, r=account2, ts=datetime.now(), amount=money)
            self.transactions.append(tx)
            return True
        else:
            raise ValueError("Not enough funds")
        
    def top_k_outgoing(self,k):
        transfers = filter(lambda x: x.type == 'transfer',self.transactions)
        amt=defaultdict(int)
        for tx in transfers:
            amt[tx.s]+=tx.amount
        sorted_outgoing = sorted(amt.items(), key=lambda kv:(kv[1],kv[0]), reverse=True)
        return sorted_outgoing[:k]
    
    def schedule(self, scheduled_tx: Tx):
        if scheduled_tx.ts >= datetime.now():
            self.scheduled_transactions.append(scheduled_tx)
    
    def remove_schedule(self,tx:Tx):
        try:
            self.scheduled_transactions.remove(tx)
        except ValueError:
            raise ValueError('Aint no tx to remove')
    
    def run_scheduled(self):
        now = datetime.now()
        due_txs = filter(lambda x: x.ts <= now,self.scheduled_transactions)
        if due_txs:
            for tx in due_txs:
                if tx.type == 'transfer':
                    self.transfer(account1=tx.s,account2=tx.r,money=tx.amount)
                elif tx.type == 'deposit':
                    self.deposit(account=tx.r,money=tx.amount)
    
    def merge(self, account1, account2):
        self._validate_account(account1), self._validate_account(account2)
        new_balance=self.balances[account1]+self.balances[account2]
        self.balances[account1] = 0
        self.balances[account2] = 0
        new_account=len(self.balances)
        self.balances.append(new_balance)
        for i,tx in enumerate(self.transactions):
            if tx.r == account1 or tx.s == account1:
                tx.original_account = account1
                tx.r = new_account
                self.transactions[i] = tx
            
            if tx.r == account2 or tx.s == account2:
                tx.original_account = account2
                tx.r = new_account
                self.transactions[i] = tx
            
        for i,tx in enumerate(self.scheduled_transactions):
            if tx.r == account1 or tx.s == account1:
                tx.original_account = account1
                tx.r = new_account
                self.scheduled_transactions[i] = tx
            
            if tx.r == account2 or tx.s == account2:
                tx.original_account = account2
                tx.r = new_account
                self.scheduled_transactions[i] = tx

bank = Bank([10,20,30,40,50])
bank.deposit(0,3000)
bank.transfer(0,1,1000)
bank.transfer(0,4,1000)
bank.transfer(1,2,900)
tx_schedule = datetime.now()+timedelta(seconds=1)
tx_scheduled = Tx('transfer',0,1,tx_schedule,500)
bank.schedule(tx_scheduled)
sleep(2)
bank.remove_schedule(tx_scheduled)
bank.run_scheduled()
bank.merge(0,4)
for tx in bank.transactions: print(tx)