# Subject: This is GMOcoin.publicAPI's feature provided by below code.
# Apiref: https://api.coin.z.com/docs/#ws-ticker Refalence at symbol.

import websocket
import json as js

from threading import Thread
import time

from logging import getLogger, StreamHandler, DEBUG
defalut_logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
defalut_logger.setLevel(DEBUG)
defalut_logger.addHandler(handler)
defalut_logger.propagate = False

# 指定したホストとメッセージを設定しWebSocket通信を開始する
class ConnectionWebSocket():
    def __init__(self,host,tickerLog=None,logger=None):#self!=websocket
        logger = logger or defalut_logger

        websocket.enableTrace(True)
        self.__ws = websocket.WebSocketApp(host)

        def on_open(self):#self==websocket
            message = {
                "command": "subscribe",
                "channel": "ticker",
                "symbol": "BTC_JPY"
            }
            def run(*args):#self==websocket
                logger.debug("Thread starting...")
                AvoidRequestTooManyError = time
                for i in range(4):
                    # send the message, then wait
                    # so thread doesn't exit and socket
                    # isn't closed
                    self.send(js.dumps(args[0]))
                    AvoidRequestTooManyError.sleep(10)

                self.close()
                logger.debug("Thread terminating...")

            Thread(target=run,args=(message,)).start()

        def on_message(self, message):#self==websocket
            logger.debug("### websocket_on_message ###")
            #logger.debug(self,message)
            if tickerLog != None:
                tickerLog(self, message)

        def on_error(ws, error):
            logger.error("### websocket_Error ###")
            logger.error(ws," : ", error)
            ws.close()

        def on_close(self):#self==websocket
            logger.debug("### websocket_closed ###")

        self.__ws.on_open = on_open
        self.__ws.on_message = on_message
        self.__ws.on_error = on_error
        self.__ws.on_close = on_close
    def run(self):#self!=websocket
        #スレッド開始
        Thread(target=self.__ws.run_forever).start()
        #NOTE:2つのWsを動作させたい場合、sendが非同期でRequest too manyになる可能性

    def pose(self):#self!=websocket
        return()#スレッド一時停止

    def stop(self):#self!=websocket
        return()#スレッド終了

    def changeMessage(self):
        return()



if __name__ == "__main__" :
    import sys
    if len(sys.argv) < 2:
        host = "wss://api.coin.z.com/ws/public/v1"
    else:
        host = sys.argv[1]

    cws=ConnectionWebSocket(self,host,logger=defalut_logger)
    cws.run()
