# telegram-lkmex-rates

[![GitHub Super-Linter](https://github.com/jokeru/telegram-lkmex-rates/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

If you own [LKMEX](https://docs.maiar.exchange/maiar-exchange-features/locked-mex-insights/what-is-LKMEX/) and you want to cash out or simply swap them for `EGLD` or `MEX`, one way of doing it is by using the 2 telegram bots: one for EGLD swaps and one for MEX swaps.  


## PreReqs

* your [telegram api_id](https://core.telegram.org/api/obtaining_api_id)


## Setup

The `main.py` script will impersonate your personal telegram account to get the latest `LKMEX` rates from the following two LKMEX Trading Bots:  
- [lkmex_trade_bot](https://t.me/LKMEX_Trade_Bot?start=5034333397)  
- [lkmex_egld_trade_bot](https://t.me/LKMEX_EGLD_Trade_Bot?start=5034333397)  

You can play with the online version of the script [here](https://replit.com/@jokeru/telegram-lkmex-rates#main.py).  
Remember to add your `API_ID` and `API_HASH` secrets to the replit project.  

For local development, you can use this [Dockerfile](Dockerfile) to build your image:  
```bash
docker build --tag telegram-lkmex-rates:0.1.0 .
docker run \
   --env API_ID=foo \
   --env API_HASH=bar \
   --tty \
   --interactive \
  telegram-lkmex-rates:0.1.0
```

### Output
```raw
Please enter your phone (or bot token): +123456789012
Please enter the code you received: 12345
Signed in successfully as John Doe
1 LKMEX = 0.369 MEX
1m LKMEX = 0.545 EGLD
```
