# This file is part stock_location_only_child module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class StockLocationOnlyChildTestCase(ModuleTestCase):
    'Test Stock Location Only Child module'
    module = 'stock_location_only_child'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            StockLocationOnlyChildTestCase))
    return suite
