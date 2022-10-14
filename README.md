# Python Service in Windows

Working example on creating a Python service in Windows

Tested on Windows 11 Enterprise 22621

## Usage

```
Usage: 'Agent.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
Options for 'install' and 'update' commands only:
--username domain\username : The Username the service is to run under
--password password : The password for the username
--startup [manual|auto|disabled|delayed] : How the service starts, default = manual
--interactive : Allow the service to interact with the desktop.
--perfmonini file: .ini file to use for registering performance monitor data
--perfmondll file: .dll file to use when querying the service for
performance data, default = perfmondata.dll
Options for 'start' and 'stop' commands only:
--wait seconds: Wait for the service to actually start or stop.
If you specify --wait with the 'stop' option, the service
and all dependent services will be stopped, each waiting
the specified period.
```

## Service Pre-requisites

Copy the following files:

```
C:\...\Python\Python310\Lib\site-packages\pywin32_system32\pythoncom310.dll
C:\...\Python\Python310\Lib\site-packages\pywin32_system32\pywintypes310.dll
```

to

```
C:\...\Python\Python310\Lib\site-packages\win32
```

## Service Code

Inherit from WinService and override the start, stop, and main methods.

## Service Installation

```
python Agent.py install
Installing service Agent
```

## Service Start

```
net start Agent
The Agent service is starting.
The Agent service was started successfully.
```
