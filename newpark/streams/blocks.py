# Flex Block
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class NavBlock(blocks.StructBlock):
    """ Block for Navigation Cards """

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=60)),
                ("button_page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )
    class Meta:
        template = "streams/nav_card_block.html"
        icon = "placeholder"
        label = "Navigation Block"
    