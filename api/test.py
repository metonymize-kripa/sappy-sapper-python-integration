# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0
# https://svelte.dev/tutorial/tick
# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0

from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import json
API_URL = 'https://www.insuremystock.com/'
SKILL_MAP = {'range':'options/range/', 'ape':'options/kelly/', 'doom':'options/doom/' , 'volume':'stocks/volume/', 'prob_pct':'options/prob_pct/'}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        curr_date = str(datetime.date(datetime.now()))
        api_output = {'main_point':'',
                      'main_class':'neutral',
                      'description':'',
                      'supporting_data':'',
                      'secondary_point':'',
                      'secondary_class':'neutral',
                      'secondary_description':'' }

        if "input_cmd" in dic:
            if dic["input_cmd"] == 'WTF':
                message = '{"symbol":"H🥚dl."}'
            else:
                cmd_list = dic["input_cmd"].strip().split()
                skill = "range"
                symbol = cmd_list[0].lower()
                if len(cmd_list) > 1:
                    skill = cmd_list[0].lower()
                try:
                    if skill == 'range':
                        api_output = make_range_response(symbol, api_output)
                    elif skill == 'doom':
                        api_output = make_doom_response(symbol, api_output)
                    elif skill == 'volume':
                        api_output = make_volume_response(symbol, api_output)
                    elif skill == 'ape':
                        api_output = make_ape_response(symbol, api_output)
                    else:
                        api_output['main_point'] = f"Invalid Command - {skill}"
                    #message = f'{{"symbol":"{my_stock.ticker}", "prob_up":{prob_move}, "price":"{round(my_stock.price)}","low":"{round(low)}","high":"{round(high)}"}}'
                except:
                    api_output['main_point'] = f"Invalid Command - {skill}"
        else:
            api_output['main_point'] = f"Bro, you need to type in sumthin"
        self.wfile.write(json.dumps(api_output,default=str)))
        return

def make_range_response(symbol, resp_dict):
    api_end_point = f"{API_URL}{SKILL_MAP['range']}{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['main_point'] = f'${round(input_dict["low_range"])} - ${round(input_dict["high_range"])}'
        resp_dict['description'] = '1Wk Price Band, Options implied @ 75% Prb.'
        if input_dict['prob_up' > 0.6]:
            resp_dict['main_class'] = 'bullish'
        elif input_dict['prob_up' < 0.4]:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = f'Now@ ${round(input_dict["price"])}'
        resp_dict['secondary_point'] = f'{input_dict["volume"]/input_dict["avg_10d_volume"]:.2f}x adv (input_dict["volume_pct"] %ile)'
        if input_dict['volume_pct' > 55]:
            resp_dict['secondary_class'] = 'bullish'
        elif input_dict['volume_pct' < 45]:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['secondary_description'] =  'Current relative volume'
    return resp_dict

def make_doom_response(symbol, resp_dict):
    api_end_point = f"{API_URL}{SKILL_MAP['doom']}{symbol}/?days=30&percent=5"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['main_point'] = f'Crash Index @{round(100*input_dict["prob_down"])}'
        resp_dict['description'] = 'Options implied Prb. of 5%👇 in month ahead'
        if input_dict['prob_down' < 0.1]:
            resp_dict['main_class'] = 'bullish'
        elif input_dict['prob_down' > 0.2]:
            resp_dict['main_class'] = 'bearish'
    return resp_dict

def make_ape_response(symbol, resp_dict):
    api_end_point = f"{API_URL}{SKILL_MAP['ape']}{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['main_point'] = f"Don't put more than {round(input_dict['kelly']*100)}% in this stonk"
        resp_dict['description'] = """Apes together but heed sage <a href="https://en.wikipedia.org/wiki/Kelly_criterion"> Kelly's advice</a>"""
    return resp_dict

def make_volume_response(symbol, resp_dict):
    api_end_point = f"{API_URL}{SKILL_MAP['volume']}{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        adv_x_volume = input_dict["volume"]/input_dict["avg_10d_volume"]
        resp_dict['main_point'] = f'{adv_x_volume:.2f}x adv'
        resp_dict['description'] = 'Relative Volume based on 10 days average'
        if adv_x_volume > 1:
            resp_dict['main_class'] = 'bullish'
        elif adv_x_volume < 0.7:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = f'Now@ {(input_dict["volume"])}'
        resp_dict['secondary_point'] = input_dict["percentile"]
        if input_dict['volume_pct' > 55]:
            resp_dict['secondary_class'] = 'bullish'
        elif input_dict['volume_pct' < 45]:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['secondary_description'] =  'Current volume percentile'
    return resp_dict

# def get_expiries_bracket(ticker, num_of_days):
#     c = Call(ticker)
#     expiries = c.expirations
#     curr_date = str(datetime.date(datetime.now()))
#     longer_expiry = expiries[-1]
#     shorter_expiry = expiries[0]
#     shorter_day_bound = (datetime.strptime(shorter_expiry,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
#     longer_day_bound = (datetime.strptime(longer_expiry,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
#     for i in expiries:
#         days_to_exp = abs(datetime.strptime(i,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
#         if days_to_exp < num_of_days and days_to_exp > shorter_day_bound  :
#             shorter_day_bound = days_to_exp
#             shorter_expiry = i
#             longer_day_bound = days_to_exp
#             longer_expiry = i
#         elif days_to_exp >= num_of_days:
#             longer_day_bound = days_to_exp
#             longer_expiry = i
#             break;
#     shorter_weight = 1;
#     if longer_day_bound != shorter_day_bound:
#         shorter_weight = (longer_day_bound - num_of_days) / (longer_day_bound - shorter_day_bound)
#     return {'shorter_expiry':shorter_expiry,'longer_expiry':longer_expiry,'shorter_day_bound':shorter_day_bound,'longer_day_bound':longer_day_bound, 'shorter_weight':shorter_weight}
#
# def get_strike_bracket(call_object, price_target):
#     strikes = call_object.strikes
#     higher_strike = strikes[0]
#     lower_strike = strikes[0]
#     if price_target < strikes[0]:
#         return (-1,-1)
#     if price_target > strikes[-1]:
#         return (-10,-10)
#     for i in strikes:
#         if i < price_target and i > lower_strike:
#             lower_strike = i
#             higher_strike = i
#         elif i >= price_target:
#             higher_strike = i
#             break;
#     lower_weight = 1
#     if higher_strike != lower_strike:
#         lower_weight = (higher_strike - price_target)/(higher_strike - lower_strike)
#     return {'lower_strike':lower_strike,'higher_strike':higher_strike, 'lower_weight':lower_weight}
# def get_atm_ivol(s, ndays=30):
#     symbol = s.ticker
#     expiry_dict = get_expiries_bracket(symbol, ndays)
#     #First Shorter One
#     x = expiry_dict['shorter_expiry']
#     shorter_call = Call(symbol,d=int(x[0:2]),m=int(x[3:5]),y=int(x[6:10]))
#     strike_dict = get_strike_bracket(shorter_call, s.price)
#     shorter_call.set_strike(strike_dict['lower_strike'])
#     lower_vol = shorter_call.implied_volatility()
#     shorter_call.set_strike(strike_dict['higher_strike'])
#     higher_vol = shorter_call.implied_volatility()
#     shorter_ivol = lower_vol*strike_dict['lower_weight'] + higher_vol*(1-strike_dict['lower_weight'])
#     #Now longer One
#     x = expiry_dict['longer_expiry']
#     longer_call = Call(symbol,d=int(x[0:2]),m=int(x[3:5]),y=int(x[6:10]))
#     strike_dict = get_strike_bracket(longer_call, s.price)
#     longer_call.set_strike(strike_dict['lower_strike'])
#     lower_vol = longer_call.implied_volatility()
#     longer_call.set_strike(strike_dict['higher_strike'])
#     higher_vol = longer_call.implied_volatility()
#     longer_ivol = lower_vol*strike_dict['lower_weight'] + higher_vol*(1-strike_dict['lower_weight'])
#     implied_ivol = shorter_ivol*expiry_dict['shorter_weight'] + longer_ivol*(1-expiry_dict['shorter_weight'])
#     one_sigma_move_ndays_day = implied_ivol*math.sqrt(ndays/365)
#     return (implied_ivol, one_sigma_move_ndays_day)
#
# def get_probability_move(symbol:str, n_days:int, percent:float):
#     c = Call(symbol)
#     curr_date = str(datetime.date(datetime.now()))
#     expiries = c.expirations
#     expiry_to_use = expiries[0]
#     for i in expiries:
#         days_to_exp = abs(datetime.strptime(i,'%d-%m-%Y') - datetime.strptime(curr_date,'%Y-%m-%d')).days
#         expiry_to_use = i
#         if days_to_exp >= n_days:
#             break
#     my_delta = get_delta(symbol, percent, expiry_to_use)
#     return {"move_percent":percent, 'expiry':expiry_to_use, "prob_down":my_delta['delta_down'],"prob_up":my_delta['delta_up'] }
#
# def get_delta(symbol:str, percent_move:float, expiry:str):
#     s = Stock(symbol)
#     up_px = s.price*(1+percent_move/100)
#     down_px = s.price*(1-percent_move/100)
#     call = Call(symbol,d=int(expiry[0:2]),m=int(expiry[3:5]),y=int(expiry[6:10]))
#     up_delta_dict = get_strike_bracket(call, up_px)
#     call.set_strike(up_delta_dict['lower_strike'])
#     delta1 = call.delta()*up_delta_dict['lower_weight']
#     call.set_strike(up_delta_dict['higher_strike'])
#     delta2 = call.delta()*(1-up_delta_dict['lower_weight'])
#     delta_up_move = delta1 + delta2
#
#     put = Put(symbol,d=int(expiry[0:2]),m=int(expiry[3:5]),y=int(expiry[6:10]))
#     down_delta_dict = get_strike_bracket(put, down_px)
#     put.set_strike(down_delta_dict['lower_strike'])
#     delta1 = -put.delta()*down_delta_dict['lower_weight']
#     put.set_strike(down_delta_dict['higher_strike'])
#     delta2 = -put.delta()*(1-down_delta_dict['lower_weight'])
#     delta_down_move = delta1 + delta2
#     return {'delta_up':delta_up_move,'delta_down':delta_down_move}
