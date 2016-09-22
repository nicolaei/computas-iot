import requests


class Switch:
    def __init__(self, username, password, ip, id):
        self.url = "http://%s:%s@%s:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_%s/" % (username, password, ip, id)

    def _command(self, command):
        r = requests.get(self.url + "command/" + command)

    def on(self):
        self._command("on")

    def off(self):
        self._command("off")


