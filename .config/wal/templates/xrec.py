## Template to add xresources colors to qtile, first is for widget's, second for layouts
## (Really just borders) 

colors = [["{color1}", "{color1}"], # panel background
          ["{color2}", "{color2}"], # background for current screen tab
          ["{color3}", "{color3}"], # font color for group names
          ["{color4}", "{color4}"], # border line color for current tab
          ["{color5}", "{color5}"], # border line color for other tab and odd widgets
          ["{color6}", "{color6}"], # color for the even widgets
          ["{color7}", "{color7}"]] # window name


layout_theme = {{
    "border_width": 2,
    "margin": 5,
    "border_focus": "{color7}",
    "border_normal": "{color6}" 
}}
