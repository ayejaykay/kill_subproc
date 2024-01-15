import multiprocessing
import subprocess
import queue
import time

tcl_location = "python"

def run_tcl(q):
    kill_flag = False
    not_running = True
    data = ""
    while(not kill_flag):
        try:
            if not_running:
                print("Starting test script")
                sp = subprocess.Popen([tcl_location, "test_script.py"])
                not_running = False
            elif data == "KILL":
                print("Killing subprocess")
                sp.terminate()
                sp.wait()
                kill_flag = True

            data = q.get(block=False)
        except queue.Empty:
            pass
    
def file_rw():
    while(1):
        print("I would be doing something here")
        time.sleep(1)

    
def terminate(p1, p2, q):
    q.put("KILL")
    p1.terminate()
    p1.join()
    p2.terminate()
    p2.join()



def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=run_tcl, args=((q,)))
    p2 = multiprocessing.Process(target=file_rw)

    p1.start()
    p2.start()


    time.sleep(10)

    q.put("KILL")
    time.sleep(5)
    print("Killing processes")
    p1.terminate()
    p2.terminate()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()