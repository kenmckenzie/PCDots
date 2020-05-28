# PCDots
![Screenshot](screenshot/screenshot.png)

My personal dotfiles for various tiling window managers plus assorted apps. Used on Arch so your mileage may vary on other distro's. (Although any arch based distro SHOULD work)

I use user templates for Pywal extremely heavily. in other words. many of the config files are actually in the ~/.config/wal/Templates folder, they need to be symlinked to their usual locations for them to work. 

A good portion of the window manager's and apps I use have been edited or patched in order to make use of xresources, so if not planning to use pywal please set your colors there to avoid alot of manual configuration

Unfortunately there is alot of manual work required to get the config as displayed, am planning to write a script to do the heavy lifting in future.

# Recomended Apps
- dwm, qtile, bspwm or i3wm gapps (My current favorite is qtile)

- dmenu (I have a custom build if wanted)

- spotifytui

- ranger

- conky (Symlink needed)

- Polybar

- Pywal(By far the most important, I love this app)

- wpgtk (Needed to theme gtk via pywal schemes)

- dunst (Create a symlink from the /.cache/Wal/dunstrc to the dunst config folder for theming to work) 

- xwallpaper 

- st or urxvt (config is set assuming you use st though, build is in repos)

- zsh + oh-my-zsh

-  yay (not needed but manually building everythings a pain )

- lx-appearance (Not strictly needed but makes config abit easier)

* - rofi 

- nvim


Note that I predominantly use Hack Nerd Font so please make sure that is installed or
adjust accordingly (The fonts I use are included but it is obviously better to use your package manager to install fonts) 


