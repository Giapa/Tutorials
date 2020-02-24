# BobTheFishSetup

![alt text](https://github.com/Giapa/BobTheFishSetup/blob/master/Screenshot%20from%202020-02-24%2013-57-43.png)

## A simple guide of installing and configuring Bob The Fish

## My example: 

### Step 1 : Installing fish

```bash
sudo apt-add-repository pps:fish-shell/release-3
sudo apt update
sudo apt install fish
```

Once you have installed fish you can run it by doing ```fish ```

### Step 2 : Set fish as default shell

Check the fish path by typing:
```bash
which fish
```

Then type:
```bash
chsh -s <path>
```

If that doesn't work, you can add fish to /bin/ by doing and adding path to /etc/shells. If you have no permission then ```sudo```

```bash
cp <path> /bin/fish
vim /etc/shells #Add /bin/fish to the file
chsh -s /bin/fish
```

If you want to switch back to bash just type:
```bash
chsh -s /user/bash
```

### Installing oh my fish

You can install oh my fish(omf) by typing:

```bash
curl -L https://get.oh-my.fish | fish
```

In order for that to work you need to have 'git' and 'curl' installed. If those are missing you can simply do:

```bash
sudo apt install git
sudo apt install curl
```

### Installing bob the fish

Inside fish shell just type:
```bash
omf install bobthefish
```

You can customize your bobthefish by playing with the config file. If the config.fish does not exist, you can create it and configure it.

```bash
touch .config/fish/config.fish
```

Open the config.fish file with a text editor or do ```vim ./config/fish/config.fish``` like a macho man

Then add the following lines:
```
set -g theme_display_user yes
set -g theme_display_hostname yes
set -g theme_display_date no
set -g theme_nerd_fonts yes
set -g theme_color_scheme nord
set -g theme_display_cmd_duration no
```

In order for the icons to be rendered properly, you need to download some nerd fonts. The best option is [RobotoMono Nerd Font](https://www.nerdfonts.com/font-downloads) . After downloading the font, extract them into .fonts folder. You can make the folder by typing ```mkdir .fonts```. After droping the fonts into the folder you can enable them by doing:

```bash
fc-cache -f -v
```

Then you need to change the font of your terminal emulator. Right click to open the settings and find the default profile. Enable custom fonts and choose the font you just downloaded.

## Bonus:

Another awsome tool is ```lsd``` which is the ```ls``` command with icons. You can download the lsd command by clicking [here](https://github.com/Peltoche/lsd/releases). Choose the lsd_0.16.0_amd64.deb. Then install it. 

If you want the additional flex you can install 'neonfetch'
```bash
sudo apt install neofetch
```
If you want 'neofetch' to run everytime you open a new terminal you can add 'neofetch' at the end of the ```config.fish``` file
## Important config

Alias is everything. You can put aliases in order to write less. Alias is binding a command with a specific string

For example:
```
alias shutdown='shutdown now'
```
This means that when typing shutdown the command shutdown now will be executed.

Some usefull aliases are:

```
alias shutdown='shutdown now'
alias python='python3'
alias pip='pip3'
alias ls='lsd'
alias la='lsd --all'
```
All these commands need to be put inside the ```config.fish``` file

## More info

[Fish shell](https://github.com/fish-shell/fish-shell)

[Oh my fish](https://github.com/oh-my-fish/oh-my-fish)

[Bob the fish](https://github.com/oh-my-fish/theme-bobthefish)

[Nerd fonts](https://www.nerdfonts.com/font-downloads)

[LSD command](https://github.com/Peltoche/lsd)

[Neofetch](https://github.com/dylanaraps/neofetch)
