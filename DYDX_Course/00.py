from dydx3.constants import API_HOST_GOERLI, API_HOST_Mainnet
from decouple import config

#!!!! SELECT MODE  !!!!
MODE = "Development" 

# Close all open postions and orders
ABORT_ALL_POSITIONS = False

# Find Cointergrated Pairs
FIND_COINTERGFATED_PAIRS = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window 
WINDOW = 21

# Threshold - Opening 
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_THRESH = 1000
USD_MIN_COLLATERAL = 1880

# Threshold - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum address
ETHEREUM_ADDRESS = "0x30BB83FEcf0c44eC9a0B1F40fD6b6ee8d131134B"

STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET")
DYDX_PASSPHRASE_TESTNET = config("DYDX_PASSPHRASE")

# KEYS Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_TESTNET
DYDX_PASSPHRASE_TESTNET = DYDX_PASSPHRASE_TESTNET
                                                                                    