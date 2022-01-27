#!/usr/bin/env python3
from integration.test import IntegrationTest

class TestBlockProduction(IntegrationTest):
    def description(self):
        return "Wait until at least 5 block are produced"

    def run(self):
        self._parachain.subscribe_block_headers(
            self._subscription_handler,
            include_author=False
        )


    def _subscription_handler(
        self,
        block_info,
        update_number,
        subscription_id
    ):
        if block_info['header']['number'] >= 5:
            return update_number
