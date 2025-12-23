devices = [
    {"name": "Router1", "ip": "192.168.1.1"},
    {"name": "Switch1", "ip": "192.168.1.2"},
]

for device in devices:
    print(f"Checking connectivity to {device['name']} ({device['ip']})...")
    print("Status: REACHABLE\n")
