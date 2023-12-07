class NetworkDevice:
    def __init__(self, device_id, device_type, ip_address):
        self.device_id = device_id
        self.device_type = device_type
        self.ip_address = ip_address
        self.is_secure = True
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def remove_vulnerability(self, vulnerability):
        self.vulnerabilities.remove(vulnerability)


class Router(NetworkDevice):
    def __init__(self, device_id, ip_address):
        super().__init__(device_id, "Router", ip_address)
        self.connected_devices = []

    def connect_device(self, device):
        self.connected_devices.append(device)


class Switch(NetworkDevice):
    def __init__(self, device_id, ip_address):
        super().__init__(device_id, "Switch", ip_address)
        self.connected_devices = []

    def connect_device(self, device):
        self.connected_devices.append(device)


class Firewall(NetworkDevice):
    def __init__(self, device_id, ip_address):
        super().__init__(device_id, "Firewall", ip_address)
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_rule(self, rule):
        self.rules.remove(rule)


class Server(NetworkDevice):
    def __init__(self, device_id, ip_address, server_type):
        super().__init__(device_id, "Server", ip_address)
        self.server_type = server_type  # e.g., 'File Server', 'Web Server'


class Workstation(NetworkDevice):
    def __init__(self, device_id, ip_address, user):
        super().__init__(device_id, "Workstation", ip_address)
        self.user = user


# Example of creating and connecting network devices
router = Router("router_1", "192.168.1.1")
firewall = Firewall("firewall_1", "192.168.1.2")
switch = Switch("switch_1", "192.168.1.3")
server = Server("server_1", "192.168.1.4", "File Server")
workstation = Workstation("workstation_1", "192.168.1.5", "Alice")

router.connect_device(firewall)
router.connect_device(switch)
switch.connect_device(server)
switch.connect_device(workstation)
