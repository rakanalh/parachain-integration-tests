#!/usr/bin/env python3
import sys
import json

from integration.system import System

def main():
    if len(sys.argv) == 1:
        print("Please provide the path to the config file")
        exit()

    filename = sys.argv[1]
    try:
        config = json.load(open(filename))
    except Exception as ex:
        print(f"Could not read config file: {ex}")
        exit()

    tests_package = config.get("tests_package", "")
    relaychain_url = config.get("relaychain_url", "")
    parachain_url = config.get("parachain_url", "")

    try:
        system = System(relaychain_url, parachain_url, tests_package)
    except Exception as e:
        print("error", e)
        return

    system.run()


if __name__ == "__main__":
    main()
