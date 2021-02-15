# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import functools

from trytond.i18n import gettext
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.exceptions import UserError


class Location(metaclass=PoolMeta):
    __name__ = 'stock.location'

    unique_children = fields.Boolean("Unique children")

    @classmethod
    def validate(cls, locations):
        super(Location, cls).validate(locations)
        for location in locations:
            if location.unique_children and len(location.childs) > 1:
                raise UserError(
                    gettext('stock_location_only_child.msg_only_child'))
