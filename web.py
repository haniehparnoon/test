import websocket,json

#اگر بخوایم یه کوین خاصی رو بگیریم و همچنین براش تایم بزاریم مثلا هر 1دیقه باید url ما این باشه
#socket = f'wss://stream.binance.com:9443/ws/{symbol}@@kline_<interval>'
#واین نکته که وقتی زمان میدیم بهش نمیتونیم بگیم کل کوینارو بده یا من پیدا نکردم ولی اگر کل کوینارو بخوایم از miniTicker@arrاستفاده میکنیم
#مثالاشم کامنت کردم پایین
# داکیومنتشم اینه
# https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
# coin_name ='btcusdt'
# time_req = '4h'
#socket = f'wss://stream.binance.com:9443/ws/{coin_name}@@kline_<time>'
#اگر میخواید کل اطلاعاتو نمایش بده توی on_message همه چی رو بردارید فقط message رو پرینت کنید

from file_Handler import FileHandler
add_to_csv_file = FileHandler("Coins.csv")
socket = f'wss://stream.binance.com:9443/ws/!miniTicker@arr'
def on_message(ws,message):
    json_message = json.loads(message)
    for i in json_message :
        data={}
        e = i['e']
        s = i['s']
        l =i['l']
        h=i['h']
        data ={'time':e ,"Symbol":s ,"low":l,"high":h}
        add_to_csv_file.add_to_file(data)

        print(data)

    # print(message)
def on_close(ws):
    print("close")
ws = websocket.WebSocketApp(socket,on_message=on_message ,on_close=on_close)
ws.run_forever()