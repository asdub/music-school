# Flex Block
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_color_panel.blocks import NativeColorBlock


class NavBlock(blocks.StructBlock):
    """ Block for Navigation Cards """

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ('color', NativeColorBlock(default="#000000")),
                ("title", blocks.CharBlock(required=True, max_length=60)),
                ("button_page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )
    class Meta:
        template = "streams/nav_card_block.html"
        icon = "placeholder"
        label = "Navigation Block"
    