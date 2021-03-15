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
        resp_dict['description'] = 'ExDiv: '+input_dict["skill_output"]["exdiv"]+'; '+'Next dividend payout on '+input_dict["skill_output"]["nextpaydate"]
        #resp_dict['description'] = '+Next dividend payout on '+input_dict["skill_output"]["nextpaydate"]
        resp_dict['supporting_data'] = ''
        resp_dict['secondary_point'] = f'{100*float(input_dict["skill_output"]["divyield"]):.2f}%'
        resp_dict['secondary_description'] =  f'Annual dividend yield, estimate as of {input_dict["datetime"]}'
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
        if 'error' in input_dict:
            resp_dict['main_point'] = "Option data is unavailable"
            return resp_dict
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'''${round(input_dict["low_range"])} - ${round(input_dict["high_range"])}<a class="card-button text-white bg-primary bd-dark" on:click="getAPIData('call',{symbol})" href="">sell call</a>'''
        resp_dict['description'] = 'Expected stock price range for next 7 days'
        if float(input_dict['prob_up']) > 0.6:
            resp_dict['main_class'] = 'bullish'
        elif float(input_dict['prob_up']) < 0.4:
            resp_dict['main_class'] = 'bearish'
        resp_dict['supporting_data'] = f'Current stock price: ${round(input_dict["price"])}'
        resp_dict['secondary_point'] = f'{input_dict["today_volume"]/input_dict["avg_10d_volume"]:.2f} times'
        if int(input_dict['volume_pct']) > 55:
            resp_dict['secondary_class'] = 'bullish'
        elif int(input_dict['volume_pct']) < 45:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['meter_value'] = int(input_dict['volume_pct'])
        resp_dict['secondary_description'] =  'Relative Volume based on past 10 days average'
        resp_dict['explain'] =  "FatNeo calculates the possible future price of stock based on option prices. Option prices are, in a way, market's way of predicting stock price. We use some really cool math to do the complicated calculations for you and find the range the stock will fall in with a 75% probability"
    return resp_dict

def make_crypto_response(symbol, resp_dict):
    api_end_point = f"{API_URL}crypto/range/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'${round(input_dict["low_range"]):,} - ${round(input_dict["high_range"]):,}'
        resp_dict['description'] = '1Wk Price Band, Historical implied @ 75% Prb.'
        resp_dict['supporting_data'] = f'Now@ ${round(input_dict["price"]):,}'
        resp_dict['secondary_point'] = f'{input_dict["today_volume"]/input_dict["avg_10d_volume"]:.2f} times'
        resp_dict['secondary_description'] =  'Relative Volume based on 10 days average'
    return resp_dict

def make_doom_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/doom/{symbol}/?days=30&percent=5"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        if 'error' in input_dict:
            resp_dict['main_point'] = "Option data is unavailable"
            return resp_dict
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f'Crash Index @{round(100*input_dict["prob_down"])}'
        resp_dict['description'] = 'Options implied Prb. of 5%👇 in month ahead'
        prob_down = float(input_dict['prob_down'])
        if prob_down < 0.1:
            resp_dict['main_class'] = 'bullish'
        elif prob_down > 0.2:
            resp_dict['main_class'] = 'bearish'

    return resp_dict

def make_ape_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/kelly/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        if 'error' in input_dict:
            resp_dict['main_point'] = "Option data is unavailable"
            return resp_dict
        resp_dict['symbol'] = symbol
        resp_dict['main_point'] = f"Consider Kelly-efficient bet sizing of: {round(input_dict['kelly']*100)}% "
        resp_dict['description'] = "Experimental feature"
        prob_up = float(input_dict['prob_up'])
        if prob_up > 0.6:
            resp_dict['main_class'] = 'bullish'
        elif prob_up < 0.4:
            resp_dict['main_class'] = 'bearish'
        prob_up_percent = round(prob_up*100)
        resp_dict['secondary_point'] = f"Probability of upside:@{prob_up_percent}"
        resp_dict['meter_value'] = prob_up_percent

    return resp_dict

def make_twitter_response(symbol, resp_dict):
    api_end_point = f"{API_URL}sentiment/twitter/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        twitter_index = round(input_dict['twitter_index'])
        resp_dict['main_point'] = f"Twitter sentiment index is : {twitter_index}% "
        resp_dict['description'] = "Experimental feature: Real time twitter sentiment"
        if int(twitter_index) > 20:
            resp_dict['main_class'] = 'bullish'
        elif int(twitter_index) < -20:
            resp_dict['main_class'] = 'bearish'
        resp_dict['meter_value'] = twitter_index
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
        percentile = int(input_dict['percentile'])
        resp_dict['secondary_point'] = f'Now@{percentile}'
        if percentile > 55:
            resp_dict['secondary_class'] = 'bullish'
        elif percentile < 45:
            resp_dict['secondary_class'] = 'bearish'
        resp_dict['meter_value'] = percentile

        resp_dict['secondary_description'] =  'Current volume percentile'
    return resp_dict

def make_call_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/call_trades/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        if 'error' in input_dict:
            resp_dict['main_point'] = "Option data is unavailable"
            return resp_dict
        resp_dict['symbol'] = symbol
        best_call = input_dict["best_call"]
        best_spread = input_dict["best_spread"]

        if best_call and 'strike' in best_call:
            resp_dict['main_point'] = f'${best_call["strike"]} Strike Call Expiring on {datetime.strptime(best_call["expiry"], "%d-%m-%Y").strftime("%d %b")}'
            resp_dict['description'] = "This is the optimal covered call to sell"
            resp_dict['supporting_data'] = f'Current option price: ${best_call["bid"]}'
            if best_call["using_last"] == "true":
                resp_dict['supporting_data'] = f'Current option price: ${best_call["bid"]} (**USING STALE DATA**)'
            resp_dict['main_class'] = 'bullish'
        else:
            resp_dict['main_point'] = "Call data is unavailable"
        if best_spread:
            resp_dict['secondary_point'] = f'Buy ${best_spread["strike_to_buy"]} strike call and sell ${best_spread["strike_to_sell"]} strike call'
            resp_dict['secondary_description'] = "This is the optimal call spread to sell"
            if best_spread["spread_using_last"] == "true":
                resp_dict['secondary_description'] = "This is the optimal call spread to sell (**USING STALE DATA**)"
            resp_dict['secondary_class'] = 'bullish'
        resp_dict['explain'] =  "FatNeo calculates the possible future price of stock based on option prices. Option prices are, in a way, market's way of predicting stock price. We use some really cool math to do the complicated calculations for you and find the optimal calls and spread for you. "
    return resp_dict

def make_put_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/put_trades/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        if 'error' in input_dict:
            resp_dict['main_point'] = "Option data is unavailable"
            return resp_dict
        resp_dict['symbol'] = symbol
        best_put = input_dict["best_put"]
        best_spread = input_dict["best_spread"]

        if best_put and 'strike' in best_put:
            resp_dict['main_point'] = f'${best_put["strike"]} Strike Put Expiring on {datetime.strptime(best_put["expiry"], "%d-%m-%Y").strftime("%d %b")}'
            resp_dict['description'] = "This is the optimal put to sell"
            resp_dict['supporting_data'] = f'Current option price: ${best_put["bid"]}'
            if best_put["using_last"] == "true":
                resp_dict['supporting_data'] = f'Current option price: ${best_put["bid"]} (**USING STALE DATA**)'
            resp_dict['main_class'] = 'bullish'
        else:
            resp_dict['main_point'] = "Put data is unavailable"
        if best_spread:
            resp_dict['secondary_point'] = f'Buy ${best_spread["strike_to_buy"]} strike put and sell ${best_spread["strike_to_sell"]} strike put'
            resp_dict['secondary_description'] = "This is the optimal put spread to sell"
            if best_spread["spread_using_last"] == "true":
                resp_dict['secondary_description'] = "This is the optimal put spread to sell (**USING STALE DATA**)"
            resp_dict['secondary_class'] = 'bullish'
        resp_dict['explain'] =  "FatNeo calculates the possible future price of stock based on option prices. Option prices are, in a way, market's way of predicting stock price. We use some really cool math to do the complicated calculations for you and find the optimal puts and spread for you. "
    return resp_dict

def make_gamma_response(symbol, resp_dict):
    api_end_point = f"{API_URL}options/gamma/{symbol}"
    resp = requests.get(api_end_point)
    if resp.ok: #Good response from FastAPI
        input_dict = resp.json()
        resp_dict['symbol'] = symbol
        shares = input_dict["stock_float"]
        gamma_1 = input_dict["gamma_1"]
        strike_1 = input_dict["strike_1"]
        gamma_2 = input_dict["gamma_2"]
        strike_2 = input_dict["strike_2"]
        gamma_1_perc = gamma_1*100/shares
        gamma_2_perc = gamma_2*100/shares
        expiry_use = datetime.strptime(input_dict["expiry_to_use"], "%Y-%m-%d").strftime("%d %b")
        resp_dict['main_point'] = f'Best Gamma Squeeze candidate: {input_dict["strike_1"]} Strike Call, Expiry: {expiry_use}'
        resp_dict['description'] = "Maximum gamma squeeze at this strike"
        resp_dict['supporting_data'] = f'Gamma Squeeze Ratio @ {gamma_1_perc:.2f}%'
        if gamma_1_perc > 10:
            resp_dict['main_class'] = 'bullish'
        resp_dict['secondary_point'] = f'Next Best Gamma Squeeze candidate: {input_dict["strike_2"]} Strike Call, Expiry: {expiry_use}'
        resp_dict['secondary_description'] = f'Gamma Squeeze Ratio @ {gamma_2_perc:.2f}%'
        if gamma_2_perc > 10:
            resp_dict['secondary_class'] = 'bullish'
        resp_dict['explain'] =  "Gamma Squeeze happens when the Open Interest in the option is high and stock approches the strike. As stock nears the strike the market makers rush to hedge the position. Higher the open interest more the hedging demand and that pushes the stock up (or down) a lot.<br> GME is a classic example. The Gamma Squeeze Ratio is the percentage of float market makers would need ot hedge the position as the stock price approaces the strike. Any number over 5% is a good for the squeeze"

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
                'put':make_put_response,
                'div':make_div_response,
                'div2':make_div2_response,
                'dive':make_dive_response,
                'twitter':make_twitter_response,
                'crypto':make_crypto_response,
                'gamma':make_gamma_response}


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
                      'meter_value':-1,
                      'secondary_description':'',
                      'explain':"" }

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
