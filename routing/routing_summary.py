"""
ip1 = '192.168.16.1/24'
ip2 = '192.168.17.1/24'
ip3 = '192.168.18.25/29'
"""
print("Please input ip in proper format(x.x.x.x/x): ")
ip_list = []
ip_bin_list = []
while True:
    ip = input()
    if ip:
        ip_split = ip.split('.')
        # 转换成二进制，扩展成8位长的二进制
        ip_list.append(ip)
    else:
        break
