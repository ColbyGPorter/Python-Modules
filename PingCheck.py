import pythonping
from pythonping import ping

IpList = ['1.1.1.1', '10.10.10.10']

for DeviceIP in IpList:
    #Remove/Add verbose=True to hide/show all ping responses
    #Example --- response_list = ping(DeviceIP, count=5, verbose=True)
    response_list = ping(DeviceIP, count=5, timeout=1)
    if response_list.packet_loss > 0:
        loss_rate = response_list.packet_loss * 100
        loss_rate_str = str(loss_rate)
        # print(loss_rate_str)
        print(DeviceIP + " is experiencing " + loss_rate_str + "% packet loss.")
        print("")
    else:
        print(DeviceIP + " is online.")
        print("")
