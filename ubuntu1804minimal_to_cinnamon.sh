sudo apt remove -y \
gedit \
gedit-common \
gnome-bluetooth \
gnome-font-viewer \
gnome-getting-started-docs \
gnome-initial-setup \
gnome-menus \
gnome-session-bin \
gnome-session-canberra \
gnome-shell \
gnome-shell-extension-appindicator \
gnome-shell-extension-ubuntu-dock \
gnome-software \
gnome-software-common \
gnome-startup-applications \
nautilus \
nautilus-sendto

sudo apt update

sudo apt install -y \
lightdm \
cinnamon \
git

sudo apt autoremove -y
sudo apt upgrade -y
sudo apt autoremove -y

sudo snap install snap-store
