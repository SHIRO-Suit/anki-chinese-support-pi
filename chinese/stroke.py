# Copyright © 2025 Nicolas Corrieri <corrieripro@gmail.com>
#
# This file is part of Chinese Support 3.
#
# Chinese Support 3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support 3 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support 3.  If not, see <https://www.gnu.org/licenses/>.

def get_stroke_order(hanzi: str) -> str:
    mdbg_base_url = "https://www.mdbg.net/chinese/rsc/img/stroke_anim/"
    file_extension = ".gif"
    css_class = "stroke"
    img_tags = []

    for char in hanzi:
        # Check if the character is a valid Chinese character
        if ord(char) > 19968:
            anim_url = f"{mdbg_base_url}{ord(char)}{file_extension}"
            img_tag = f'<img class="{css_class}" src="{anim_url}" alt="{char} animation" />'
            img_tags.append(img_tag)

    return "\n".join(img_tags)