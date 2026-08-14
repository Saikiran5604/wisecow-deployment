#!/usr/bin/env python3
#System Health Monitoring Script:
import os
import shutil
import time
from datetime import datetime

LOG_FILE = "system_health.log"
THRESHOLD = 80.0

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"
    print(formatted_msg)
    with open(LOG_FILE, "a") as f:
        f.write(formatted_msg + "\n")

def check_system_health():
    log_message("=== Starting System Health Check ===")

    # 1. CPU Usage (via load averages)
    load1, _, _ = os.getloadavg()
    cpu_count = os.cpu_count() or 1
    cpu_usage_pct = (load1 / cpu_count) * 100
    log_message(f"CPU Usage (Load-based): {cpu_usage_pct:.2f}%")
    if cpu_usage_pct > THRESHOLD:
        log_message(f"[ALERT] CPU usage exceeds threshold! ({cpu_usage_pct:.2f}%)")

    # 2. Memory Usage (via /proc/meminfo)
    mem_info = {}
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                parts = line.split(':')
                if len(parts) == 2:
                    mem_info[parts[0].strip()] = int(parts[1].split()[0])
        
        total_mem = mem_info.get('MemTotal', 1)
        free_mem = mem_info.get('MemFree', 0) + mem_info.get('Buffers', 0) + mem_info.get('Cached', 0)
        used_mem = total_mem - free_mem
        mem_usage_pct = (used_mem / total_mem) * 100
        log_message(f"Memory Usage: {mem_usage_pct:.2f}% (Used: {used_mem // 1024} MB / Total: {total_mem // 1024} MB)")
        if mem_usage_pct > THRESHOLD:
            log_message(f"[ALERT] Memory usage exceeds threshold! ({mem_usage_pct:.2f}%)")
    except Exception as e:
        log_message(f"[ERROR] Could not read memory info: {e}")

    # 3. Disk Space Usage
    total, used, free = shutil.disk_usage("/")
    disk_usage_pct = (used / total) * 100
    log_message(f"Disk Usage (/): {disk_usage_pct:.2f}% (Used: {used // (2**30)} GB / Total: {total // (2**30)} GB)")
    if disk_usage_pct > THRESHOLD:
        log_message(f"[ALERT] Disk usage exceeds threshold! ({disk_usage_pct:.2f}%)")

    # 4. Running Processes Count
    try:
        process_count = len([name for name in os.listdir('/proc') if name.isdigit()])
        log_message(f"Running Processes Count: {process_count}")
    except Exception as e:
        log_message(f"[ERROR] Could not count processes: {e}")

    log_message("=== Health Check Complete ===\n")

if __name__ == "__main__":
    check_system_health()