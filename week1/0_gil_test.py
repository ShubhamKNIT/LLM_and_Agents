# This test is used to check whether the GIL is enabled or not.
import time
import threading
import sysconfig

def worker():
    for i in range(5):
        print(f"Worker {threading.current_thread().name} is working...")
        time.sleep(1)

if __name__ == "__main__":
    
    # Check GIL status
    if bool(sysconfig.get_config_var("Py_GIL_DISABLED")):
        print("GIL is disabled.")
    else:
        print("GIL is enabled.")

    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, name=f"Thread-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads have finished.")