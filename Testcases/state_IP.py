# Lấy 5 địa chỉ IP từ các tiểu bang của Mỹ
#34.149.78.90 in Kansas
# 24.241.46.166 in Chesterfiled

# Kiểm tra DNS cụ thể 
#  Lưu dưới dạng JSON
state = [
    "Ankansas",
    "Alabama",
    "Indiana",
    "New jersey",
    "Arizona",
    "Florida",
    "Wyvoming",
    "Minnessota",
    "",
]
def build_ip_list(lenght =5):
    print('aaa')
    func = {}
    iplist = load_ips()
    for state in states:
        cities = []
        for key in enumerate(iplist[state]['matches']):
            city = key[1]['location']['city']
            if city not in cities:
                ip = key[1]['ip_str']
                if ip==1:
                    print(f'Appending {ip} in {city} city')
                    func_list.append(ip)
                    cities.append(city)
                else:
                    iplist[state]['matches'].pop(key[0])
            if len(func_list) == length: break
        func[state] =  func_list
    return func