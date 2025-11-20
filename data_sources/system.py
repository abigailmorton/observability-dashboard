import psutil
import platform
import shutil
from datetime import datetime

def get_system_stats():
    """
    Basic local system stats for the dashboard.
    """
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=0.5)

    # Memory
    mem = psutil.virtual_memory()
    mem_used_gb = round(mem.used / (1024**3), 2)
    mem_total_gb = round(mem.total / (1024**3), 2)
    mem_percent = mem.percent

    # Disk (root filesystem)
    disk = shutil.disk_usage("/")
    disk_used_gb = round(disk.used / (1024**3), 2)
    disk_total_gb = round(disk.total / (1024**3), 2)
    disk_percent = round(disk.used / disk.total * 100, 1)

    # Uptime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    uptime_hours = round(uptime.total_seconds() / 3600, 1)

    return {
        "os": f"{platform.system()} {platform.release()}",
        "hostname": platform.node(),
        "cpu_percent": cpu_percent,
        "mem_used_gb": mem_used_gb,
        "mem_total_gb": mem_total_gb,
        "mem_percent": mem_percent,
        "disk_used_gb": disk_used_gb,
        "disk_total_gb": disk_total_gb,
        "disk_percent": disk_percent,
        "uptime_hours": uptime_hours,
    }

if __name__ == "__main__":
    print(get_system_stats())
