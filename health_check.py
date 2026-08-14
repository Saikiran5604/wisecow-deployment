#!/usr/bin/env python3
#Application Health Checker
import urllib.request
import urllib.error
from datetime import datetime

# Target application URL (e.g., Wisecow app endpoint)
APP_URL = "http://localhost:4499"
TIMEOUT_SECONDS = 5

def check_application_health(url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Checking application status at: {url}")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'AppHealthChecker/1.0'})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            status_code = response.getcode()
            # Standard successful HTTP status codes
            if 200 <= status_code < 400:
                print(f"[{timestamp}] Status: UP  (HTTP Status Code: {status_code})")
                return True
            else:
                print(f"[{timestamp}] Status: DOWN  (HTTP Status Code: {status_code})")
                return False
                
    except urllib.error.HTTPError as e:
        print(f"[{timestamp}] Status: DOWN  (HTTP Error Code: {e.code})")
        return False
    except urllib.error.URLError as e:
        print(f"[{timestamp}] Status: DOWN  (Connection Failed: {e.reason})")
        return False
    except Exception as e:
        print(f"[{timestamp}] Status: DOWN  (Unexpected Error: {e})")
        return False

if __name__ == "__main__":
    check_application_health(APP_URL)