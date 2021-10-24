from flask import render_template, abort, request, jsonify
from app import app
import requests
from main_page.models import PhotoDb, Temp
import random


# @app.route('/')
# def index():
#     """Python Program to Get IP Address"""
#     # ip1= jsonify({'ip': request.remote_addr})
#     # xx = request.remote_addr
#     # gg = request.remote_user
#     ip2 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
#     # ip = requests.get('https://api.ipify.org').text
#
#     # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#     #     print('22',request.environ['REMOTE_ADDR'])
#     # else:
#     #     print('11',request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
#
#     # return f'request.remote_addr   {xx} request.remote_user  {gg} request.environ.get  {ip2} requests.get(https:  {ip} '
#
#     # query = '103.194.67.94'
#     # query = ip
#     # url = f"http://ip-api.com/json/{query}"
#     # payload = "{\"ips\": [\"1.1.1.1\", \"1.2.3.4\"]}"
#     # response_ip = requests.request("POST", url, data=payload)
#     # y=response_ip.json()
#
#     """get weathrer condition  """
#
#     key = '53d7f1dde8564a69838135859212907'
#     q = ip2
#     url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={q}&aqi=no'
#     response = requests.request("POST", url)
#
#     weather_json = response.json()
#     current_temp = weather_json["current"]["temp_c"]
#     print(current_temp)
#     temps = Temp.query.all()
#     for temp in temps:
#         if temp.mintemp < current_temp < temp.maxtemp:
#             condition = temp
#             photo = random.choice(condition.photo)
#             return render_template('main.html', weather_json=weather_json, photo=photo)
#     abort(404)
#     return render_template('main.html', weather_json=weather_json, photo=photo)
