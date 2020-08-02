sudo apt remove -y \
gedit \
gedit-common \
gnome-characters \
gnome-font-viewer \
gnome-getting-started-docs \
gnome-initial-setup \
gnome-logs \
gnome-menus \
gnome-session-bin \
gnome-session-canberra \
gnome-session-common \
gnome-shell \
gnome-shell-common \
nautilus \
nautilus-sendto

sudo apt update

sudo apt install -y --no-install-recommends \
lightdm \
cinnamon \
net-tools \
git \
curl

sudo apt autoremove -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt-get clean

reboot
