#!/bin/python3
import time
from light_switch import Switch

if __name__ == "__main__":
    switch = Switch("admin", "WelcometoCX01", "10.0.1.11", "6-0-37")

    switch.off()
    time.sleep(1)
    switch.on()
