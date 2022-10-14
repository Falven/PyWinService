import servicemanager
import socket
import win32event
import win32service
import win32serviceutil


class WinService(win32serviceutil.ServiceFramework):
    '''Base class to create a Python Windows Service'''

    _svc_name_ = "JnJ Service"
    _svc_display_name_ = "JnJ Service"
    _svc_description_ = "JnJ service description"

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Windows Service Constructor
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Override with pre-start logic
        '''
        pass

    def stop(self):
        '''
        Override with pre-stop logic
        '''
        pass

    def main(self):
        '''
        Override with Main logic
        '''
        pass


if __name__ == '__main__':
    WinService.parse_command_line()
