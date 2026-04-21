#!/usr/bin/env python3

"""
Linux specific `make run` watcher using inotify.
"""

import os
import subprocess
import ctypes
import struct
import select
import time

# inotify constants
IN_CLOSE_WRITE = 0x00000008
IN_MOVED_TO = 0x00000080
MASK = IN_CLOSE_WRITE | IN_MOVED_TO

# int wd, uint32 mask, uint32 cookie, uint32 len
EVENT_FMT = 'iIII'
EVENT_SIZE = struct.calcsize(EVENT_FMT)


def watch():
    libc = ctypes.CDLL("libc.so.6")
    fd = libc.inotify_init()
    if fd < 0:
        return

    libc.inotify_add_watch(fd, b".", MASK)
    # Ignore output files to prevent infinite loops
    ignored = {'test.json', 'new_settings.json', 'fs.py'}
    last_trigger = 0

    print("Watching for changes (excluding outputs)...")

    try:
        while True:
            r, _, _ = select.select([fd], [], [], 1.0)
            if fd not in r:
                continue

            raw_data = os.read(fd, 1024)
            i = 0
            while i + EVENT_SIZE <= len(raw_data):
                _, mask, _, n_len = struct.unpack(EVENT_FMT,
                                                  raw_data[i:i+EVENT_SIZE])
                name = raw_data[i+EVENT_SIZE:i+EVENT_SIZE+n_len]
                name = name.decode().strip('\x00')
                i += EVENT_SIZE + n_len

                # Filter: extension check + ignored files + debounce
                valid_ext = name.endswith(('.py', '.json'))
                is_src = name not in ignored and not name.startswith('.')

                # 0.5s debounce to handle burst events from editors
                if valid_ext and is_src and (time.time() - last_trigger > 0.5):
                    print(f"{name} changed. Running 'make run'...")
                    subprocess.run(['make', 'run'])
                    last_trigger = time.time()
                    break
    except KeyboardInterrupt:
        print("\nWatcher stopped.")
    finally:
        os.close(fd)


if __name__ == "__main__":
    watch()
