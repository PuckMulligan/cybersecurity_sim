from flask import Flask, jsonify, request
from random import randint
from network_components import Router, Switch, Firewall, Server, Workstation

app = Flask(__name__)

def generate_random_mac():
    """
    Generates a random MAC address for simulation purposes.
    
    Returns:
        str: A randomly generated MAC address.
    """
    return "02:00:00:%02x:%02x:%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))

def network_scan(ip):
    """
    Simulates a network scan within a given IP range. In this simulation,
    the function generates a list of devices with random IP and MAC addresses.
    
    Args:
        ip (str): The IP range to scan. In this simulation, it's not used.

    Returns:
        list: A list of dictionaries, each representing a device with 'ip' and 'mac' keys.
    """
    simulated_devices_count = randint(5, 10)  # Determine the number of devices to simulate
    devices = []

    for _ in range(simulated_devices_count):
        # Generate a random IP and MAC address for each simulated device
        ip = f"192.168.1.{randint(1, 254)}"
        mac = generate_random_mac()
        devices.append({'ip': ip, 'mac': mac})

    return devices

# Initialize simulated network components with example parameters
router = Router("router_1", "192.168.1.1")
firewall = Firewall("firewall_1", "192.168.1.2")
server = Server("server_1", "192.168.1.4", "File Server")
workstations = [Workstation(f"workstation_{i}", f"192.168.1.{i+5}", f"User{i}") for i in range(1, 6)]

@app.route('/')
def home():
    """
    A simple homepage route.

    Returns:
        str: A message indicating the backend is running.
    """
    return 'Cybersecurity Simulation Backend Running'

@app.route('/network/status')
def network_status():
    """
    Endpoint that provides the current status of the network. It returns the status of routers,
    firewalls, servers, and workstations in the simulated network.

    Returns:
        json: A JSON object containing the status of each network component.
    """
    # Constructing a response with the status of each network component
    network_status = {
        "router": {"ip": router.ip_address, "status": "online"},
        "firewall": {"ip": firewall.ip_address, "status": "online"},
        "server": {"ip": server.ip_address, "status": server.is_secure},
        "workstations": [{"ip": ws.ip_address, "status": ws.is_secure} for ws in workstations]
    }
    return jsonify(network_status)

@app.route('/scan')
def scan():
    """
    Endpoint to initiate a simulated network scan. This route triggers the network_scan function
    and returns a list of simulated network devices.

    Returns:
        json: A JSON object containing a list of simulated devices found in the scan.
    """
    ip_range = "192.168.1.1/24"  # IP range for simulation purposes
    devices = network_scan(ip_range)
    return jsonify({"devices": devices})

@app.route('/intrusion/scan')
def simulate_scan_intrusion():
    """
    Simulate a basic network scan intrusion.
    This function generates a simulated intrusion report.

    Returns:
        json: A JSON object describing the simulated intrusion.
    """
    # Define the intrusion behavior
    intrusion_behavior = {
        "type": "Unauthorized Access Attempt - Network Scan",
        "purpose": "To identify active devices and potential vulnerabilities in the network.",
        "behavior_characteristics": {
            "scanning_targets": "Entire network (192.168.1.1/24)",
            "scanning_methods": "ICMP ping requests to identify active hosts.",
            "frequency": "Periodic, every 5 minutes.",
            "stealth_level": "Low (aggressive scanning)",
            "detection_criteria": "Detection occurs if more than 20 ping requests are received within 1 minute."
        },
        "response": "The simulation logs the intrusion attempt. Users are notified of the intrusion and prompted to respond.",
        "scalability": "This basic intrusion behavior can be expanded to include more advanced scanning techniques and responses in future simulation scenarios."
    }

    # Simulate the intrusion scenario
    # Intrusion logic
    
    # For now, the intrusion behaviour returns a JSON
    return jsonify(intrusion_behavior)

if __name__ == '__main__':
    app.run(debug=True)
