# Flex Block
from typing_extensions import Required
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_color_panel.blocks import NativeColorBlock
from wagtail_icon_picker.blocks import FontAwesomeIconPickerBlock


class NavBlock(blocks.StructBlock):
    """ Block for Navigation Cards """

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ('color', NativeColorBlock(default="#072660")),
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


class GridBlock(blocks.StructBlock):
    """ Block for Grid Layout """

    grids = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ('color', NativeColorBlock(default="#072660")),
                ("cover", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False   )),
                ("intro", blocks.TextBlock(required=False)),
                ("body", blocks.RichTextBlock(required=False)),
                ("buttons", blocks.ListBlock(blocks.StructBlock(
                    [
                        ("icon", FontAwesomeIconPickerBlock(required=False)),
                        ("button_text", blocks.CharBlock(required=False, max_length=60)),
                        ("button_page", blocks.PageChooserBlock(required=False)),
                        ("button_url", blocks.URLBlock(required=False)),
                    ]
                ))),
            ]
        )
    )
    class Meta:
        template = "streams/grid_block.html"
        icon = "placeholder"
        label = "Grid Block"


class TableBlock(blocks.StructBlock):
    """ Standard Block for Pages """

    table = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("cover", ImageChooserBlock(required=False)),
                ("heading", blocks.CharBlock(required=False, max_length=100)),
                ("titles", blocks.ListBlock(blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(required=False)),
                    ], block_counts = {
                        'title': {'max_num': 4},
                    }
                ))),
                ("rows", blocks.ListBlock(blocks.StructBlock(
                    [
                        ("course", blocks.CharBlock(required=False)),
                        ("class_length", blocks.CharBlock(required=False)),
                        ("duration", blocks.CharBlock(required=False)),
                        ("price", blocks.CharBlock(required=False)),
                    ]
                ))),
            ], block_counts = {
                'titles': {'max_mun': 1},
            }
        )
    )
    class Meta:
        template = "streams/table_block.html"
        icon = "placeholder"
        label = "Table Content Block"


class StandardBlock(blocks.StructBlock):
    """ Standard Block for Pages """

    standard = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("cover", ImageChooserBlock(required=False)),
                ("heading", blocks.CharBlock(required=False, max_length=100)),
                ("subtext", blocks.TextBlock(required=False)),
                ("listtext", blocks.ListBlock(blocks.StructBlock(
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
        template = "streams/standard_list_block.html"
        icon = "placeholder"
        label = "Multi Content Block"


class ListBlock(blocks.StructBlock):
    """ Block for About Page Lists """

    list = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("cover", ImageChooserBlock(required=False)),
                ("heading", blocks.CharBlock(required=False, max_length=100)),
                ("subtext", blocks.TextBlock(required=False)),
                ("listtext", blocks.ListBlock(blocks.StructBlock(
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
        label = "Multi Content Block"


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
        label = "Single Content Block"
    

class ButtonBlock(blocks.StructBlock):
    """ Block for Including Nav Buttons"""

    buttons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("icon", FontAwesomeIconPickerBlock(required=True)),
                ("button_text", blocks.CharBlock(required=True, max_length=60)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )
    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Button Block"