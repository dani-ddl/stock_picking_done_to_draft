# -*- coding: utf-8 -*-

from odoo import _, models, api
from odoo.exceptions import UserError


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_back_to_draft(self):
        if self.filtered(lambda m: m.state != 'done'):
            raise UserError(_("Error"))
        self.write({'state': 'draft'})


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_back_to_draft(self):
        moves = self.mapped('move_lines')
        moves.action_back_to_draft()
