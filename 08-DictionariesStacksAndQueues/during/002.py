mobile = {
    "OS": "Android",
    "CPU": "Helio G95",
    "RAM": ["6GB", "8GB"],
    "Camera": {"main": "48MP", "ultrawide": "8MP", "macro": "2MP"},
    "battery": 5000,
    "memory": ["64GB", "128GB"]
}

for key, value in mobile.items():
    print(f"{key}: {value}")