import threading
import time

class FPSCheck(object):
    _tick = 0

    def __init__(self):
        pass

    def start(self):
        threading.Thread(target=self.tick_counter, daemon=True).start()
        while True:
            tick = "".join(reversed([v if i % 3 or i == 0 else v + "," for i, v in enumerate(reversed(list(str(self._tick))))]))
            print(f"FPS: {tick} | {self._tick}")
            self._tick = 0
            time.sleep(1)

    def tick_counter(self):
        ### !!!!!!!!!!!!!!!!!!!!!!!!!!!
        ### !!! Edit your code here !!!
        ### !!!!!!!!!!!!!!!!!!!!!!!!!!!

        while True:
            self._tick += 1

def main():
    try:
        input("Press Enter to start. CTRL + C to exit.")
    
        fpscheck = FPSCheck()
        fpscheck.start()
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
