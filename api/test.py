# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0
# https://svelte.dev/tutorial/tick
# https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0

from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import requests
API_URL = 'https://www.insuremystock.com/'
FAT_NEO_API_URL = 'https://api.fatneo.com/parse'


def make_wsb_response(symbol, resp_dict):
    api_end_point = f"{FAT_NEO_API_URL}/{symbol} WSB"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'{int(100*float(input_dict["skill_output"]))}%'
        resp_dict['description'] = 'Percentage of mentions on r/wsb'
        if float(input_dict['skill_output']) > 0.01:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['skill_output']) < 0.001:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = ''
        resp_dict['secondary_point'] = ''
        resp_dict['secondary_description'] =  f'Pulled as of {input_dict["datetime"]}'
    return resp_dict

def make_wise_response(symbol, resp_dict):
    api_end_point = f"{FAT_NEO_API_URL}/{symbol} WISE"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'{int(100*float(input_dict["skill_output"]))}%'
        resp_dict['description'] = 'Percentage of mentions with curated social media analysts'
        if float(input_dict['skill_output']) > 0.01:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['skill_output']) < 0.001:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = ''
        resp_dict['secondary_point'] = ''
        resp_dict['secondary_description'] =  f'Pulled as of {input_dict["datetime"]}'
    return resp_dict

def make_div2_response(symbol, resp_dict):
    api_end_point = f"{FAT_NEO_API_URL}/{symbol} DIV2"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'${float(input_dict["skill_output"]):.2f}'
        resp_dict['description'] = 'Updated dividend announced this year'
        resp_dict['supporting_data'] = ''
        resp_dict['secondary_point'] = ''
        resp_dict['secondary_description'] =  f'Pulled as of {input_dict["datetime"]}'
    return resp_dict

def make_dive_response(symbol, resp_dict):
    api_end_point = f"{FAT_NEO_API_URL}/{symbol} DIVE"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'${float(input_dict["skill_output"]["nextestpayout"]):.2f}'
        resp_dict['description'] = 'Payout expected on '+input_dict["skill_output"]["nextpaydate"]
        resp_dict['supporting_data'] = ''
        resp_dict['secondary_point'] = f'{100*float(input_dict["skill_output"]["nextestpayout"]):.2f}%'
        resp_dict['secondary_description'] =  f'Dividend yield, estimate as of {input_dict["skill_output"]["divyield"]}'
    return resp_dict

def make_div_response(symbol, resp_dict):
    api_end_point = f"{API_URL}stocks/dividend/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        if float(input_dict["div"]) == 0:
            resp_dict['main_point'] = "{symbol} has had no dividend. A shame"
        else:
            resp_dict['main_point'] = f'Last dividend: ${float(input_dict["div"]):.2f}'
            resp_dict['description'] = f'Last Dividend Date : {datetime.strptime(input_dict["div_date"], "%Y-%m-%d").strftime("%b %d")}'
            if input_dict["div_yld"]:
                resp_dict['supporting_data'] = f'Div Yield @ {100*input_dict["div_yld"]:.2f}%'

    return resp_dict

def make_range_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/range/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'${round(input_dict["low_range"])} - ${round(input_dict["high_range"])}'
        resp_dict['description'] = '1Wk Price Band, Options implied @ 75% Prb.'
        if float(input_dict['prob_up']) > 0.6:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['prob_up']) < 0.4:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = f'Now@ ${round(input_dict["price"])}'
        resp_dict['secondary_point'] = f'{input_dict["today_volume"]/input_dict["avg_10d_volume"]:.2f} times'
        if int(input_dict['volume_pct']) > 55:
            resp_dict['secondary_class'] = 'bullish'
        elif int(input_dict['volume_pct']) < 45:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['secondary_description'] =  'Relative Volume based on 10 days average'
    return resp_dict

def make_doom_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/doom/{symbol}/?days=30&percent=5"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'Crash Index @{round(100*input_dict["prob_down"])}'
        resp_dict['description'] = 'Options implied Prb. of 5%👇 in month ahead'
        if float(input_dict['prob_down']) < 0.1:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['prob_down']) > 0.2:
            resp_dict['main_class'] = 'bearish'
    return resp_dict

def make_ape_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/kelly/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f"Consider Kelly-efficient bet sizing of: {round(input_dict['kelly']*100)}% "
        resp_dict['description'] = "Experimental feature"
        if float(input_dict['prob_up']) > 0.6:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['prob_up']) < 0.4:
            resp_dict['main_class'] = 'bearish'
    return resp_dict

def make_volume_response(symbol, resp_dict):
    api_end_point = f"{API_URL}stocks/volume/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        adv_x_volume = input_dict["volume"]/input_dict["avg_10d_volume"]
        resp_dict['main_point'] = f'{adv_x_volume:.2f} times'
        resp_dict['description'] = 'Relative Volume based on 10 days average'
        if adv_x_volume > 1:
            resp_dict['main_class'] = 'bullish'
        elif adv_x_volume < 0.7:
            resp_dict['main_class'] = 'bearish'
        #resp_dict['supporting_data'] = f'Now@{(input_dict["percentile"])}'
        resp_dict['secondary_point'] = f'Now@{int(input_dict["percentile"])}'
        if float(input_dict['percentile']) > 55:
            resp_dict['secondary_class'] = 'bullish'
        elif float(input_dict['percentile']) < 45:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['secondary_description'] =  'Current volume percentile'
    return resp_dict

def make_call_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/call_trades/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        best_call = input_dict["best_call"]
        best_spread = input_dict["best_spread"]
        if best_call:
            resp_dict['main_point'] = f'${best_call["strike"]} Strike Call Expiring on {datetime.strptime(best_call["expiry"], "%d-%m-%Y").strftime("%d %b")}'
            resp_dict['description'] = "Optimal covered call to sell"
            resp_dict['supporting_data'] = f'Now@ ${best_call["bid"]}'
            if best_call["using_last"] == "true":
                resp_dict['supporting_data'] = f'Now@ ${best_call["bid"]} (**USING STALE DATA**)'
            resp_dict['main_class'] = 'bullish'
        else:
            resp_dict['main_point'] = f''
        if best_spread:
            resp_dict['secondary_point'] = f'Buy ${best_spread["strike_to_buy"]} strike call and sell ${best_spread["strike_to_sell"]} strike call'
            resp_dict['secondary_description'] = "Optimal call spread to sell given probalities implied by options"
            if best_spread["spread_using_last"] == "true":
                resp_dict['secondary_description'] = "Optimal call spread to sell given probalities (**USING STALE DATA**)"
            resp_dict['secondary_class'] = 'bullish'
    return resp_dict

#SKILL_MAP = {'range':'options/range/', 'ape':'options/kelly/','kelly':'options/kelly/','doom':'options/doom/' , 'volume':'stocks/volume/', 'prob_pct':'options/prob_pct/','wsb':'stocks/volume/', 'new2':'options/kelly/' }
FUNCTION_MAP = {'range':make_range_response, 
                'ape':make_ape_response,
                'kelly':make_ape_response,
                'doom':make_doom_response , 
                'volume':make_volume_response,
                'wsb':make_wsb_response, 
                'wise':make_wise_response, 
                'call':make_call_response, 
                'div':make_div_response,
                'div2':make_div2_response,
                'dive':make_dive_response}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        curr_date = str(datetime.date(datetime.now()))
        api_output = {'symbol':'trying..',
                      'main_point':'',
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
                    skill = cmd_list[1].lower()
                try:
                    if skill in FUNCTION_MAP:
                        api_output = FUNCTION_MAP.get(skill)(symbol, api_output)
                    else:
                        api_output['main_point'] = f"Invalid Command - {skill}"
                    #message = f'{{"symbol":"{my_stock.ticker}", "prob_up":{prob_move}, "price":"{round(my_stock.price)}","low":"{round(low)}","high":"{round(high)}"}}'
                except:
                    api_output['main_point'] = f"Seem like Invalid Command - {skill}"
        else:
            api_output['main_point'] = f"Bro, you need to type in sumthin"
        self.wfile.write((json.dumps(api_output)).encode())
        return
