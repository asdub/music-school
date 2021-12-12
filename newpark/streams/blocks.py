# Flex Block
from typing_extensions import Required
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
                ("button_url", blocks.URLBlock(required=False)),

            ]
        )
    )
    class Meta:
        template = "streams/nav_card_block.html"
        icon = "placeholder"
        label = "Navigation Block"


class ListBlock(blocks.StructBlock):
    """ Block for About Page Lists """

    list = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("cover", ImageChooserBlock(required=False)),
                ("heading", blocks.CharBlock(required=False, max_length=100)),
                ("subtext", blocks.TextBlock(required=False)),
                ("list", blocks.ListBlock(blocks.StructBlock(
                    [
                        ("text", blocks.RichTextBlock(required=False)),
                    ]
                ))),
                ("single_image", ImageChooserBlock(required=False)),
                ("image_gallery", blocks.ListBlock(blocks.StructBlock(
                    [
                        ("gallery_image", ImageChooserBlock(required=False)),
                        ("caption", blocks.CharBlock(required=False)),
                    ]
                )))
            ]
        )
    )
    class Meta:
        template = "streams/about_list_block.html"
        icon = "placeholder"
        label = "About List Block"


class SingleBlock(blocks.StructBlock):
    """ Block for About Page Single Items """

    single = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("cover", ImageChooserBlock(required=False)),
                ("heading", blocks.CharBlock(required=False, max_length=100)),
                ("subtext", blocks.TextBlock(required=False)),
                ("text", blocks.RichTextBlock(Required=False)),
                ("image", ImageChooserBlock(required=False)),

            ]
        )
    )
    class Meta:
        template = "streams/about_single_block.html"
        icon = "placeholder"
        label = "About Single Block"
    