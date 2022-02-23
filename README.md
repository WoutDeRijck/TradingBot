# Setup

To be able to run this bot, install the library alpaca-trade-api:

```
$ pip3 install alpaca-trade-api
```

Also set the environment variables (in linux):

```
export APCA_API_KEY_ID=PKDLU7JBVEEHQ9X28ZL0
export APCA_API_SECRET_KEY=mdShaWjeHEmwy3qKX2U3HwD3AwusUkap9VT9wUWA
export APCA_API_BASE_URL=https://api.alpaca.markets
export APCA_API_DATA_URL=https://data.alpaca.markets
```
For more information, see https://github.com/alpacahq/alpaca-trade-api-python


# Algorithm

For the algorithm, we use exponential averages and the macd
1. Only when the price is above the long term line, we check for buying opportunities
2. If this is fulfilled we check for a crossover from the macd line above the signal line: BUY
3. Make a sell order with a stop loss = price of long term line and a limit = 1,5 * stop loss
4. If there is a crossunder from the macd line under the signal line: SELL anyway