#!/usr/bin/env python3

class IntegrationTest:
    def __init__(self, relaychain, parachain):
        self._relaychain = relaychain
        self._parachain = parachain

    def description(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
