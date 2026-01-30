import pythonping
from pythonping import ping

IpList = ['1.1.1.1', '8.8.8.8']

for DeviceIP in IpList:
    #Remove/Add verbose=True to hide/show all ping responses
    #Example --- response_list = ping(DeviceIP, count=5, verbose=True)
    response_list = ping(DeviceIP, count=5, verbose=True)
    if response_list.success:
        print(DeviceIP + " is Alive - pythonping")
    else:
        print(DeviceIP + " is Dead - pythonping")