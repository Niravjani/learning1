from odoo import models, fields


class ArtArtwork(models.Model):
    _name = 'art.artwork'
    _description = 'Artwork'

    name = fields.Char(
        string='Artwork Name',
        required=True
    )

    artist_name = fields.Char(
        string='Artist Name',
        required=True
    )

    art_type = fields.Selection(
        [
            ('painting', 'Painting'),
            ('sculpture', 'Sculpture'),
            ('photography', 'Photography'),
            ('drawing', 'Drawing'),
            ('digital', 'Digital Art'),
            ('other', 'Other'),
        ],
        string='Art Type'
    )

    price = fields.Float(
        string='Price'
    )

    year_created = fields.Integer(
        string='Year Created'
    )

    description = fields.Text(
        string='Description'
    )

    exhibition_id = fields.Many2one(
        'art.exhibition',
        string='Exhibition',
        ondelete='cascade'
    )
