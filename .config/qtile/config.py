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

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from xrec import colors, layout_theme # see xrec.py in qtile folder
from typing import List  # noqa: F401

mod = "mod4"

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
    Key([mod], "Return", lazy.spawn("st")),
    Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "F1", lazy.spawn("atom")),
    Key([mod], "F2", lazy.spawn("brave")),
    Key([mod], "F3", lazy.spawn("thunar")),
    Key([mod], "F4", lazy.spawn("spotify")),
    Key([mod], "z" , lazy.spawn("rofimenu")),
    Key([mod, "shift"], "d", lazy.spawn("rofi -modi 'window,run,ssh,drun' -show run")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),
    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioStop", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")),

    # general volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volumenotify +5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volumenotify -5")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # music volume
#    Key(["mod4"], "XF86AudioRaiseVolume", lazy.spawn("mpc volume +5")),
#    Key(["mod4"], "XF86AudioLowerVolume", lazy.spawn("mpc volume -5")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# Standard Layout settings are moved to xrec.py to allow for theming

# apply them below
layouts = [
    #layout.Max(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Columns(),
    #layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Tile(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font = "monospace",
        fontsize = 10,
        sections = ["FIRST", "SECOND"],
        section_fontsize = 11,
        bg_color = "141414",
        active_bg = "90C435",
        active_fg = "000000",
        inactive_bg = "384323",
        inactive_fg = "a0a0a0",
        padding_y = 5,
        section_top = 10,
        panel_width = 320
        ),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font='monospace',
    fontsize=14,
    padding=0,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.LaunchBar(progs=[('rofi','rofimenu','Rofi launcher')],default_icon='/home/ulverza/Pictures/icons/arch.png', background=colors[2]),
                widget.GroupBox(
                        padding = 10,
                        active = colors[6],
                        inactive = colors[5],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "block",
                        this_current_screen_border = colors[3],
                        #this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),

                widget.Prompt(),
                widget.WindowName(
                        padding=3,
                        background=colors[2]
                        ),
                widget.Mpris2(background=colors[2],scroll_chars=50,objname='org.mpris.MediaPlayer2.spotify'),
                #widget.TextBox("default config", name="default"),
                #widget.CheckUpdates(),
                widget.CurrentLayoutIcon(),
                widget.NetGraph(
                        padding=5,
                        border_color=colors[0],
                        fill_color=colors[2],
                        graph_color=colors[2]
                        ),
                widget.Clock(padding=5,
                        format='%Y-%m-%d %a %I:%M %p'
                        ),
                widget.Systray(padding=5),
                widget.QuickExit(padding=5,
                        default_text="[  ]",
                        background=colors[0]
                        ),
            ],
            24,opacity=0.8
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
]

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
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
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
