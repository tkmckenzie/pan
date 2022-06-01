from Blockchain import Block, Blockchain, Transaction
from time import time

chain = Blockchain()
chain.add_new_transaction({'from':'system', 'to':'taylor', 'amount':100})
chain.mine()
