from serial.tools import list_ports


def serial_ports(vid_pid="10C4:EA60", str2search=None, verbose=False):
    """ Lists serial port names
        :returns:
            A list of the serial ports available on the system
COM49:USB VID:PID=10C4:EA60 SER=5 LOCATION=1-2
COM50:USB VID:PID=10C4:EA60 SER=5 LOCATION=1-1
    """
    result = []
    #print(['COM%s' % (i + 1) for i in range(256)])
    for comport in list_ports.comports():
        print('#'*50)        
        port, portDes, bus = comport
        print(f"port:{port}, portDes:{portDes}, bus:{bus}")
        if verbose:
            print(port+","+portDes+","+bus)
        bus = str.split(bus)
        print(f'bus: {bus}')
        #Todo Add check for bus location
        try:
            if bus[1] != None and vid_pid in bus[1]:
                if str2search is None or str2search in portDes:
                    result.append(port)
        except:
            pass
    return result

if __name__ == '__main__':
    # print(f'Found port {serial_ports(vid_pid="05C6:9025", str2search="Diagnostics", verbose=True)}')
    print(f'Found port {serial_ports(vid_pid="05C6:9008", str2search="QDLoader", verbose=True)}')

