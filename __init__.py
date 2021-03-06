# This file is part stock_location_only_child module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import stock

module = 'stock_location_only_child'

def register():
    Pool.register(
        stock.Location,
        module=module, type_='model')
