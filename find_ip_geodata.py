
def find_ip_location(ip_address):

    # convert input ip address to int
    long_ip_func = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
    long_ip = long_ip_func(ip_address)

    # load geoip database
    # in this file, column 0 -> start IP, column 1 -> end IP, column 13 -> geolocation
    ip_database = open("geoip_database.txtx")
    start_IP_list = []
    end_IP_dict = {}
    geodata_dict = {}
    count = 0
    try:
        for line in ip_database:
            tmp_list = line.split('\t')
            start_IP_list.append(long_ip_func(tmp_list[0]))
            end_IP_dict[count] = long_ip_func(tmp_list[1])
            geodata_dict[count] = tmp_list[13]
            count += 1
    finally:
        ip_database.close()

    # binary search
    low = 0
    high = len(start_IP_list)
    index = 0
    try:
        while low < high:
            mid = (low + high)/2
            if start_IP_list[mid] < long_ip:
                if start_IP_list[mid + 1] >= long_ip:
                    index = mid
                    break
                low = mid + 1
            elif start_IP_list[mid] > long_ip:
                if start_IP_list[mid - 1] <= long_ip:
                    index = mid
                    break
                high = mid - 1
            else:
                index = mid
    except Exception:
        return ''

    if long_ip < end_IP_dict[index]:
        return str(geodata_dict[index])
    else:
        return ''



if __name__ == '__main__':
    print(find_ip_location("8.8.8.8"))
