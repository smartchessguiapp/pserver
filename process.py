import collections
import logging
import threading
import os
import sys
import signal
import platform
import subprocess

class PopenProcess(object):
    def __init__(self, command, cwd, **kwargs):

        self._receiving_thread = threading.Thread(target=self._receiving_thread_target)
        self._receiving_thread.daemon = True
        self._stdin_lock = threading.Lock()

        popen_args = {
            "cwd": cwd,
            "stdout": subprocess.PIPE,
            "stdin": subprocess.PIPE,
            "bufsize": 1,  # Line buffering
            "universal_newlines": True,        
        }
        popen_args.update(kwargs)

        print("popen",popen_args)

        self.process = subprocess.Popen(command, **popen_args)

        self._receiving_thread.start()

    def _receiving_thread_target(self):
        while True:
            line = self.process.stdout.readline()
            if not line:
                # Stream closed.
                break

            sline = line.rstrip()
            print(sline)

        # Close file descriptors.
        self.process.stdout.close()
        with self._stdin_lock:
            self.process.stdin.close()

        # Ensure the process is terminated (not just the in/out streams).
        if self.is_alive():
            self.terminate()
            self.wait_for_return_code()

    def is_alive(self):
        return self.process.poll() is None

    def terminate(self):
        self.process.terminate()

    def kill(self):
        self.process.kill()

    def send_line(self, string):
        print("sending line",string)
        with self._stdin_lock:
            self.process.stdin.write(string + "\n")
            self.process.stdin.flush()

    def wait_for_return_code(self):
        self.process.wait()
        return self.process.returncode

    def pid(self):
        return self.process.pid

    def __repr__(self):
        return "<PopenProcess at {0} (pid={1})>".format(hex(id(self)), self.pid())