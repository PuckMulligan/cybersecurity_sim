import click
from flask import Flask, jsonify
from random import randint
from network_components import Router, Switch, Firewall, Server, Workstation

app = Flask(__name__)

# Initialize simulated network components with example parameters
router = Router("router_1", "192.168.1.1")
firewall = Firewall("firewall_1", "192.168.1.2")
server = Server("server_1", "192.168.1.4", "File Server")
workstations = [Workstation(f"workstation_{i}", f"192.168.1.{i+5}", f"User{i}") for i in range(1, 6)]

@click.command()
@click.option('--simulations', default=1, help='Number of simulations to run.')
def run_simulation(simulations):
    """Run cybersecurity simulations."""
    for _ in range(simulations):
        simulate_network_scan()

def simulate_network_scan():
    # Simulate the intrusion scenario
    intrusion_report = {
        "type": "Network Scan",
        "description": "A network scan has been detected.",
        "details": "An external device attempted to scan the network.",
        "status": "Detected",
    }

    # Log the intrusion report

    print("Simulated Network Scan Intrusion Detected:")
    print(jsonify(intrusion_report))

if __name__ == '__main__':
    run_simulation()
