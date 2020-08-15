## Template to add xresources colors to qtile, first is for widget's, second for layouts
## (Really just borders) 

colors = [["{color0}", "{color0}"], 
          ["{color1}", "{color1}"],
          ["{color2}", "{color2}"],
          ["{color3}", "{color3}"],
          ["{color4}", "{color4}"],
          ["{color5}", "{color5}"],
          ["{color6}", "{color6}"],
          ["{color7}", "{color7}"], 
          ["{color8}", "{color8}"], 
          ["{color9}", "{color9}"]] 
        

layout_theme = {{
    "border_width": 2,
    "margin": 5,
    "border_focus": "{color2}",
    "border_normal": "{color7}" 
}}

floating_theme = {{
    "border_width": 2,
    "margin": 5,
    "border_focus": "{color4}",
    "border_normal": "{color3}" 
}}

