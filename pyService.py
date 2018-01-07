import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time
import logging


class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService"
    _svc_display_name_ = "PythonService"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        f = open('c:\\Temp\\PythonService.txt', 'a')
        f.write('closing file')
        f.close()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        f = open('c:\\Temp\\PythonService.txt', 'w')
        f.write('starting service\n')
        f.close()
        self.main()

    def main(self):
        while True:
            f = open('c:\\Temp\\PythonService.txt', 'a')
            f.write('Hello at %s\n' % time.ctime())
            f.close()
            time.sleep(2)
        return


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)
