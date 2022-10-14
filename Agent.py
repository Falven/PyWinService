import time
from WinService import WinService


class Agent(WinService):

    _svc_name_ = "MissionControlAgent"
    _svc_display_name_ = "Mission Control Agent"
    _svc_description_ = "Device management capabilities for Mission Control"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            print("Hello JnJ...")
            time.sleep(5)


if __name__ == '__main__':
    Agent.parse_command_line()
