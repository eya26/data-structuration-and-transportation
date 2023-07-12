class Station:
    def __init__(self, rank, network, name, number_of_users, connections, city, district):
        self.rank = rank
        self.network = network
        self.name = name
        self.number_of_users = number_of_users
        self.connections = connections
        self.city = city
        self.district = district

data = '''...'''  # The provided data

stations = []
lines = data.strip().split('\n')
for line in lines:
    fields = line.split(';')
    rank = int(fields[0])
    network = fields[1]
    name = fields[2]
    number_of_users = int(fields[3])
    connections = fields[4:9] if fields[4:9] != ['','','','',''] else []
    city = fields[9]
    district = int(fields[10]) if fields[10] else None

    station = Station(rank, network, name, number_of_users, connections, city, district)
    stations.append(station)
