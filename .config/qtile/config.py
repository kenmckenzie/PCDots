# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# TODO, finish switching away from wal template for setting colors, 
# Longterm, split things up to different files for readibility


from libqtile.config import Key, Screen, Group, Drag, Click , ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook, extension
from xrec import colors # , layout_theme # see xrec.py in qtile folder
import json
from typing import List  # noqa: F401
from os import environ , getenv, path
# below import requires Xparser, install with pip 
import xrp
import psutil
# Get terminal from environment variables
terminal = environ.get("TERMINAL")
mod = "mod4"


# parse xresources in file, much better implementation 
xresources = path.realpath(getenv('HOME') + '/.config/.Xresources')
result = xrp.parse_file(xresources, 'utf-8')
# Set to use color[0], change if true black is wanted 
color_data = json.loads(open(getenv('HOME')+'/.cache/wal/colors.json').read())
BLACK = color_data['colors']['color0']
# BLACK = "#15181a"
# BLACK = "#1A1C1D"
RED = color_data['colors']['color1']
GREEN = color_data['colors']['color2']
YELLOW = color_data['colors']['color3']
BLUE = color_data['colors']['color4']
MAGENTA = color_data['colors']['color5']
CYAN = color_data['colors']['color6']
WHITE = color_data['colors']['color7']

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),

    # Move though groups (workspaces)
    Key([mod], "period", lazy.screen.next_group()),
    Key([mod], "comma", lazy.screen.prev_group()),

    # Restore all windows to default size ratios
    Key(
    [mod], "n",
    lazy.layout.normalize()
    ),
    # Toggle a window between minimum and maximum sizes
    Key(
    [mod], "m",
    lazy.layout.maximize()
    ),


    # Grow and shrink windows and move between them master stack like dwm, the ONLY way to do it IMO

    Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
    Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle Floating
    Key([mod, "shift"], "space",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),

    # Toggle Fullscreen
    Key([mod], "f",
    lazy.window.toggle_fullscreen()
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    # My usual program startup shortcuts
    Key([mod], "Return", lazy.spawn("st")),
    Key([mod], "d",  lazy.run_extension(extension.DmenuRun())),
    Key([mod], "F1", lazy.spawn("atom")),
    Key([mod], "F2", lazy.spawn("brave")),
    Key([mod], "F3", lazy.spawn("thunar")),
    Key([mod], "F4", lazy.spawn("spotify")),
   # Key([mod], "z" , lazy.spawn("rofimenu")),
    Key([mod], "z" , lazy.run_extension(extension.J4DmenuDesktop())),
    # Toggles compositor
    Key([mod], "t" , lazy.spawn("comp")),
    Key([mod, "shift"], "d", 
            lazy.spawn("rofi -modi 'window,run,ssh,drun' -show run")),
    Key([], "XF86AudioNext", 
            lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", 
            lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),
    Key([], "XF86AudioPlay", 
            lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioStop", 
            lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")),
    Key([mod], '0', lazy.run_extension(extension.CommandSet(
        commands={
            'lock': 'slock',
            'suspend': 'systemctl suspend && slock',
            'restart': 'reboot',
            'shutdown': 'systemctl poweroff',
            'logout': 'qtile-cmd -o cmd -f shutdown',
            'reload': 'qtile-cmd -o cmd -f restart',
            },
        ))),
    # general volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volumenotify +5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volumenotify -5")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # music volume
#    Key(["mod4"], "XF86AudioRaiseVolume", lazy.spawn("mpc volume +5")),
#    Key(["mod4"], "XF86AudioLowerVolume", lazy.spawn("mpc volume -5")),

    Key([mod], "Tab", lazy.run_extension(extension.WindowList(
        item_format="{group}: {window}",
        foreground=BLUE,
        selected_background=BLUE)),
        desc='window list'),

    # Toggle between different layouts as defined below
    Key([mod,'shift'], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]
     
group_names = [ "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 λ", "9 " ]
groups = [Group(name, layout='monadtall') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]

# append a scratchpad group
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "st", opacity=0.8),
    ]),
)

# define keys to toggle the dropdown for st
keys.extend([
    Key([mod], 'grave', lazy.group['scratchpad'].dropdown_toggle('term')),
])

# Standard Layout settings are moved to xrec.py to allow for theming

layout_theme = {
    "border_width": 2,
    "margin": 5,
    "border_focus":GREEN,
    "border_normal":BLACK 
}

floating_theme = {
    "border_width": 2,
    "margin": 5,
    "border_focus":YELLOW,
    "border_normal":BLUE 
}

# apply them below
layouts = [
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Columns(),
    #layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Max(),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
#    layout.TreeTab(
#        font = "monospace",
#        fontsize = 10,
#        sections = ["FIRST", "SECOND"],
#        section_fontsize = 11,
#        bg_color = "141414",
#        active_bg = "90C435",
#        active_fg = "000000",
#        inactive_bg = "384323",
#        inactive_fg = "a0a0a0",
#        padding_y = 5,
#        section_top = 10,
#        panel_width = 320
#        ),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font='monospace',
    fontsize=14,
    padding=0,
    background=BLACK,
)
#extension_defaults = widget_defaults.copy()
extension_defaults = dict(
    dmenu_prompt=">",
    dmenu_font='monospace',
    background=BLACK,
    foreground=GREEN,
    selected_background=GREEN,
    selected_foreground=BLACK,
    dmenu_height=24,
    dmenu_ignorecase=True
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.LaunchBar(progs=[('rofi','jgmenu_run','Rofi Launcher')],
                    default_icon='/home/ulverza/Pictures/icons/arch.png',
                    background=BLACK),
                widget.GroupBox(
                        padding = 5,
                        active = WHITE,
                        inactive = CYAN,
                        rounded = False,
                        highlight_color = YELLOW,
                        highlight_method = "block",
                        this_current_screen_border = GREEN,
                        #this_screen_border = colors [4],
                        other_current_screen_border = BLACK,
                        other_screen_border = BLACK,
                        foreground = GREEN,
                        background = BLACK,
                        disable_drag = True,
                        #hide_unused = True 
                        ),

                widget.Prompt(),
#                widget.WindowName(
#                        padding=3,
#                        background=colors[2]
#                        ),
#                 widget.Mpris(objname='org.mpris.MediaPlayer.spotify'),
                widget.TaskList(
                    padding=4,
                    highlight_method='block',
                    border=GREEN,
                    unfocused_border=BLACK,
                    background=GREEN,
                    rounded=False, 
                    margin=0,
                    icon_size=15,
                    title_width_method='uniform'
                    ),
                widget.Mpris2(display_metadata=['xesam:title', 'xesam:artist'],
                        stop_pause_text=" ",	
                        scroll_wait_intervals=30 ,	
                        background=BLACK,
                        scroll_chars=50,
                        objname='org.mpris.MediaPlayer2.spotify'),
                #widget.TextBox("default config", name="default"),
                #widget.CheckUpdates(),
                widget.CurrentLayoutIcon(),
                widget.NetGraph(
                        padding=5,
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e nmtui')},
                        border_color=BLACK,
                        fill_color=GREEN,
                        graph_color=GREEN
                        ),
                widget.Clock(padding=5,
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e calcurse')},
                        format='%Y-%m-%d %a %I:%M %p'
                        ),
                widget.Systray(padding=5),
                widget.QuickExit(padding=5,
                        default_text="[  ]",
                        background=BLACK
                        ),
            ],
            24,opacity=0.7
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
    # Really bad implemenation, replaced with xclickroot, find on github
    #Click([], "Button3", lazy.spawn("jgmenu_run"))
]

# Steam floating on all windows exept main
@hook.subscribe.client_new
def float_steam(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("Steam", "Steam")
        and (
            w_name != "Steam"
            # w_name == "Friends List"
            # or w_name == "Screenshot Uploader"
            # or w_name.startswith("Steam - News")
            or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
        )
    ):
        window.floating = True
        
@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()}
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()

@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, 'parent'):
        window.parent.minimized = False

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
],no_reposistion_match=None,**layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
