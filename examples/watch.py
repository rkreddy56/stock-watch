import robin_stocks.markets as markets
import robin_stocks.urls as urls
import time
import keyboard
import signal
import sys

while True:
    try:
            data = markets.get_top_movers(direction="down", info=None)
            #print(data[0])
            symbol_data = [
            (
                 i["symbol"],
                 i["price_movement"]["market_hours_last_movement_pct"],
                 i["price_movement"]["market_hours_last_price"],
            )
            for i in data
         ]
            print(f"** Downers ****")
            print(f"symbol\tmovement in % \t$ Last Price")
            print(f"** -Ve ****\n")
            
            for symbol in symbol_data:
                print(f"{symbol[0]}\t{symbol[1]} %\t$ {symbol[2]}")

         #print(symbol_data)

         # print("The net worth in $ {} ".format(data))
        
        #print(symbol_data)
            dataUp = markets.get_top_movers(direction="up", info=None)
            #print(dataUp)
            symbol_dataUp = [
                (
                    x["symbol"],
                    x["price_movement"]["market_hours_last_movement_pct"],
                    x["price_movement"]["market_hours_last_price"],
                )
                for x in dataUp
            ]
            print(f"\n*** Uppers *****")
            print(f"symbol\tmovement in % \t$ Last Price")
            print(f"** +Ve ****\n")
            #print(symbol_dataUp)
            for symbolup in symbol_dataUp:
                print(f"{symbolup[0]}\t{symbolup[1]} %\t$ {symbolup[2]}")

            print('\n Waitint 5 secs ...')
            time.sleep(5)
    except KeyboardInterrupt:
            print('\n Thank you for using us...')
            break