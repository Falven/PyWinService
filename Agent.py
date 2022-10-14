import time
from WinService import WinService


class Agent(WinService):

    _svc_name_ = "Agent"
    _svc_display_name_ = "Agent Display Name"
    _svc_description_ = "Agent Description"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            print("Hello Agent...")
            time.sleep(5)


if __name__ == '__main__':
    Agent.parse_command_line()
