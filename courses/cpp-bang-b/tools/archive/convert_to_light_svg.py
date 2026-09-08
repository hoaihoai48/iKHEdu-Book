import re

def convert_svg_to_light(svg_text):
    # Check if file has defs with bgGrad
    # For L13-L15 style:
    # 1. Update bgGrad:
    # stop-color="#0b0f19" -> "#FFFFFF"
    # stop-color="#111827" -> "#F8FAFC"
    # 2. Add or update stroke on background rect:
    # fill="url(#bgGrad)" rx="16" -> fill="url(#bgGrad)" stroke="#CBD5E1" stroke-width="2" rx="16"
    pass
