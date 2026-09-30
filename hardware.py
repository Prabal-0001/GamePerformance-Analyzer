from database import CPUS, GPUS


# Look through the local data and find a matching hardware name.
def find_component(database, name):
    name = name.strip().lower()
    for key, value in database.items():
        if key.lower() == name:
            return key, value
    return None, None


# Collect the hardware details entered by the user.
def get_hardware():
    print("\n--- HARDWARE CONFIGURATION ---")
    print("Known CPUs:")
    print(", ".join(CPUS.keys()))
    cpu = input("Enter CPU: ").strip()

    print("Known GPUs:")
    print(", ".join(GPUS.keys()))
    gpu = input("Enter GPU: ").strip()

    try:
        ram = int(input("Enter RAM (GB): "))
        if ram <= 0:
            raise ValueError
    except ValueError:
        print("Invalid RAM. Using 8 GB.")
        ram = 8

    cpu_name, cpu_data = find_component(CPUS, cpu)
    gpu_name, gpu_data = find_component(GPUS, gpu)

    if cpu_data is None:
        print("CPU not found in local database. Capability analysis will be limited.")
    if gpu_data is None:
        print("GPU not found in local database. Capability analysis will be limited.")

    return {
        "cpu": cpu_name or cpu,
        "cpu_data": cpu_data,
        "gpu": gpu_name or gpu,
        "gpu_data": gpu_data,
        "ram": ram
    }


# Turn the stored hardware information into a simple capability level.
def get_hardware_capability(hardware):
    cpu = hardware["cpu_data"]
    gpu = hardware["gpu_data"]

    if cpu is None or gpu is None:
        return {
            "cpu_tier": "Unknown",
            "gpu_tier": "Unknown",
            "vram": "Unknown",
            "system_tier": "Unknown",
            "summary": "Hardware was not found in the local reference data."
        }

    cpu_tier = cpu["tier"]
    gpu_tier = gpu["tier"]

    if cpu_tier >= 6 and gpu_tier >= 6 and hardware["ram"] >= 16:
        system_tier = "High"
    elif cpu_tier >= 4 and gpu_tier >= 4 and hardware["ram"] >= 8:
        system_tier = "Medium"
    else:
        system_tier = "Entry"

    if gpu["relative_score"] >= 75:
        summary = "Good capability for demanding games."
    elif gpu["relative_score"] >= 50:
        summary = "Suitable for many games with sensible settings."
    else:
        summary = "Better suited to lighter games or lower settings."

    return {
        "cpu_tier": cpu_tier,
        "gpu_tier": gpu_tier,
        "vram": gpu["vram_gb"],
        "system_tier": system_tier,
        "summary": summary
    }
