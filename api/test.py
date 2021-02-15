# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0
# https://svelte.dev/tutorial/tick
# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0

from datetime import datetime, timedelta
from wallstreet import Call, Put, Stock
from http.server import BaseHTTPRequestHandler
from urllib import parse
from scipy.stats import norm
import math

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        curr_date = str(datetime.date(datetime.now()))
        
        if "sym" in dic:
            if dic["sym"] == 'WTF':
                message = "r/Wsb eTF?\nH🥚dl."
            else:
                try:
                    my_stock = Stock(dic["sym"])
                    my_tuple = get_atm_ivol(my_stock, 7)
                    curr_price = my_stock.price
                    low = curr_price - 1.15*my_tuple[1]*curr_price
                    high = curr_price + 1.15*my_tuple[1]*curr_price
                    message = f'{{"symbol":"{my_stock.ticker}","price":"{round(my_stock.price)}","low":"{round(low)}","high":"{round(high)}"}}'
                except:
                    message = '{"symbol":"invalid_symbol"}'
        else:
            message = "Hello, stranger!"
        self.wfile.write(message.encode())
        return
def get_expiries_bracket(ticker, num_of_days):
    c = Call(ticker)
    expiries = c.expirations
    curr_date = str(datetime.date(datetime.now()))
    longer_expiry = expiries[-1]
    shorter_expiry = expiries[0]
    shorter_day_bound = (datetime.strptime(shorter_expiry,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
    longer_day_bound = (datetime.strptime(longer_expiry,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
    for i in expiries:
        days_to_exp = abs(datetime.strptime(i,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
        if days_to_exp < num_of_days and days_to_exp > shorter_day_bound  :
            shorter_day_bound = days_to_exp
            shorter_expiry = i
            longer_day_bound = days_to_exp
            longer_expiry = i
        elif days_to_exp >= num_of_days:
            longer_day_bound = days_to_exp
            longer_expiry = i
            break;
    shorter_weight = 1;
    if longer_day_bound != shorter_day_bound:
        shorter_weight = (longer_day_bound - num_of_days) / (longer_day_bound - shorter_day_bound)
    return {'shorter_expiry':shorter_expiry,'longer_expiry':longer_expiry,'shorter_day_bound':shorter_day_bound,'longer_day_bound':longer_day_bound, 'shorter_weight':shorter_weight}

def get_strike_bracket(call_object, price_target):
    strikes = call_object.strikes
    higher_strike = strikes[0]
    lower_strike = strikes[0]
    if price_target < strikes[0]:
        return (-1,-1)
    if price_target > strikes[-1]:
        return (-10,-10)
    for i in strikes:
        if i < price_target and i > lower_strike:
            lower_strike = i
            higher_strike = i
        elif i >= price_target:
            higher_strike = i
            break;
    lower_weight = 1
    if higher_strike != lower_strike:
        lower_weight = (higher_strike - price_target)/(higher_strike - lower_strike)
    return {'lower_strike':lower_strike,'higher_strike':higher_strike, 'lower_weight':lower_weight}
def get_atm_ivol(s, ndays=30):
    symbol = s.ticker
    expiry_dict = get_expiries_bracket(symbol, ndays)
    #First Shorter One
    x = expiry_dict['shorter_expiry']
    shorter_call = Call(symbol,d=int(x[0:2]),m=int(x[3:5]),y=int(x[6:10]))
    strike_dict = get_strike_bracket(shorter_call, s.price)
    shorter_call.set_strike(strike_dict['lower_strike'])
    lower_vol = shorter_call.implied_volatility()
    shorter_call.set_strike(strike_dict['higher_strike'])
    higher_vol = shorter_call.implied_volatility()
    shorter_ivol = lower_vol*strike_dict['lower_weight'] + higher_vol*(1-strike_dict['lower_weight'])
    #Now longer One
    x = expiry_dict['longer_expiry']
    longer_call = Call(symbol,d=int(x[0:2]),m=int(x[3:5]),y=int(x[6:10]))
    strike_dict = get_strike_bracket(longer_call, s.price)
    longer_call.set_strike(strike_dict['lower_strike'])
    lower_vol = longer_call.implied_volatility()
    longer_call.set_strike(strike_dict['higher_strike'])
    higher_vol = longer_call.implied_volatility()
    longer_ivol = lower_vol*strike_dict['lower_weight'] + higher_vol*(1-strike_dict['lower_weight'])
    implied_ivol = shorter_ivol*expiry_dict['shorter_weight'] + longer_ivol*(1-expiry_dict['shorter_weight'])
    one_sigma_move_ndays_day = implied_ivol*math.sqrt(ndays/365)
    return (implied_ivol, one_sigma_move_ndays_day)
