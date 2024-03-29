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

from typing import List  # noqa: F401

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from colors import * # I know I know, but it's literally a file with only variables lmao

mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Control window sizes
    Key([mod, "control"], "Left", lazy.layout.shrink_main()),
    Key([mod, "control"], "Right", lazy.layout.grow_main()),
    Key([mod, "control"], "Down", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Switch between different groups relative to your current one
    Key([mod], "Tab", lazy.screen.next_group(),
        desc="Switch to next group/workspace."),
    Key([mod], "grave", lazy.screen.prev_group(),
        desc="Switch to previous group/workspace."),

    # Control Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
        
    ])

layouts = [
    layout.MonadTall(
        margin = 18,
        border_normal = rivet_bg,
        border_focus = rivet_bg,
        border_width = 0,
        padding = 4,
    ),
    layout.Floating(
        border_width = 1,
        border_normal = rivet_grays_2,
        border_focus = rivet_grays_2,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font = 'Ubuntu',
    fontsize = 15,
    padding = 6,
    foreground = rivet_grays_2,
)

def icon_defaults():
    return {
        'fontsize':38,
        'foreground':rivet_blues_3,
        'background':rivet_bg,
    }

def toggleable_defaults():
    return {
        'background':rivet_bg,
        'close_button_location':'right',
        'fontsize':18,
        'text_closed':'',
        'text_open':'',
    }

def separator_defaults():
    return {
        'foreground':rivet_oranges_2,
        'background':rivet_bg,
        'fontsize':16,
    }

gears = widget.TextBox(
           text = "",
           **icon_defaults(),
)
gear = widget.TextBox(
           text = "",
           **icon_defaults(),
)
wrench = widget.TextBox(
           text = "",
           **icon_defaults(),
)
numberline = widget.TextBox(
           text = "",
           **icon_defaults(),
)
window_title = widget.TextBox(
           text = "",
           **icon_defaults(),
)
orange_dots_sep = widget.TextBox(
           text = "",
           **separator_defaults(),
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                orange_dots_sep,
                numberline,
                widget.GroupBox(
                    fontsize = 16,
                    font = 'Ubuntu Bold',
                    background = rivet_bg,
                    urgent_border = rivet_oranges_2,
                    active = rivet_oranges_3,
                    inactive = rivet_grays_1,
                    highlight_method = "border",
                    highlight_color = clear,
                    rounded = True,
                    border_radius = 9,
                    borderwidth = 2,
                    disable_drag = True,
                    hide_unused = True,
                    this_screen_border = clear,
                    this_current_screen_border = rivet_grays_2,
                    block_highlight_text_color = rivet_grays_2,
                    margin = 3,
                    margin_x = 10,
                ),
                orange_dots_sep,
                window_title,
                widget.WindowName(
                    empty_string_group='Desktop',
                    background = rivet_bg,
                    fontsize = 18,
                ),
                orange_dots_sep,
                widget.Battery(
                    foreground = rivet_blues_3,
                    background = rivet_bg,
                    charge_char = '',
                    discharge_char = '',
                    empty_char = '',
                    fontsize = 28,
                    format = '{char}',
                    update_interval = 1,
                ),
                widget.WidgetBox(
                    **toggleable_defaults(), 
                    widgets = [
                        widget.Battery(
                            background = rivet_bg,
                            fontsize = 18,
                            format = '{percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
                            update_interval = 45,
                        ),    
                    ],
                ),
                orange_dots_sep,
                widget.Clock(
                    background = rivet_bg,
                    foreground = rivet_blues_3,
                    font = 'Ubuntu Bold',
                    fontsize = 16,
                    format = '%I:%M\n%p',
                    padding = 5,
                ),
                widget.WidgetBox(
                   **toggleable_defaults(), 
                    widgets = [
                        widget.Clock(
                            background = rivet_bg,
                            fontsize = 18,
                            format = '%a, %B %d %Y',
                            padding = 5, 
                        ),
                    ],
                ),
            ],
            36,
            background = clear,
            foreground = clear,
            padding = 2,
            margin = [12, 12, 0, 12],
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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
#floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    #*layout.Floating.default_float_rules,
    #Match(wm_class='confirmreset'),  # gitk
    #Match(wm_class='makebranch'),  # gitk
    #Match(wm_class='maketag'),  # gitk
    #Match(wm_class='ssh-askpass'),  # ssh-askpass
    #Match(title='branchdialog'),  # gitk
    #Match(title='pinentry'),  # GPG key password entry
#])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen(['/home/ken/.loginrc/qtile_start.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
