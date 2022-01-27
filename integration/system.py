#!/usr/bin/env python3
import importlib
import inspect
from threading import Thread
from substrateinterface import SubstrateInterface

class System:
    def __init__(self, relaychain_url, parachain_url, tests_package):
        try:
            self._relaychain = SubstrateInterface(
                url=relaychain_url,
            )
        except ConnectionRefusedError:
            print("Relaychain node is not up and running")
            raise

        try:
            self._parachain = SubstrateInterface(
                url=parachain_url,
            )
        except ConnectionRefusedError:
            print("Parachain node is not up and running")
            raise

        self._tests = []

        self._discover_tests(tests_package)

    def _discover_tests(self, tests_package):
        tests_package = importlib.import_module(tests_package)
        for name, test_class in inspect.getmembers(tests_package):
            if inspect.isclass(test_class) and name.startswith("Test"):
                self._tests.append(test_class(self._relaychain, self._parachain))

        print(f"Found {len(self._tests)} tests.")
        for test in self._tests:
            print(f" - {test.__class__.__name__}: {test.description()}")

    def run(self):
        for test in self._tests:
            print(f"Run test: {test.description()}")
            thread = Thread(target=test.run)
            thread.start()
            try:
                # Wait 5 minutes for each test
                thread.join(timeout=5*60)
            except RuntimeError:
                print("Test failed")

        print("Finished")
