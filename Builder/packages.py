from utils.schemes import Packages, DistributionPackages


BASE = Packages(
	pacman=DistributionPackages(
		common=[
			"pacman-contrib", "downgrade", "libnotify", "ffmpeg","ffmpegthumbnailer", "jq", "parallel", "kitty", "fastfetch", "lsd", "bat", "brightnessctl", 
			"automake", "blueman", "bluez", "bluez-utils", "dunst", "fakeroot", "firefox", "fish", "fisher", "dpkg", "gcc", "git", "gnu-netcat", "btop", 
			"micro", "mat2", "nemo", "papirus-icon-theme", "pavucontrol", "pamixer", "pipewire", "pipewire-pulse", "pipewire-audio",
			"pipewire-jack", "pipewire-alsa", "wireplumber", "python-pyalsa", "ranger", "redshift", "reflector", "sudo", "tree", "unrar",
			"zip", "unzip", "uthash", "ark", "cmake", "clang", "gzip", "imagemagick",
			"make", "openssh", "shellcheck", "vlc", "loupe", "usbutils", "openvpn", "networkmanager-openvpn", "p7zip", "gparted",
			"sshfs", "wget", "netctl", "libreoffice", "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd", "ttf-fira-code",
        	"ttf-iosevka-nerd", "playerctl", "starship", "upower", "udiskie", "zenity", "gvfs", "qt5ct", "qt6ct",
        	"timeshift", "sddm", "qt5-graphicaleffects", "qt5-svg",  "qt5-quickcontrols2", "clipnotify",
			"xdg-desktop-portal-gtk", "code", "gnome-disk-utility", "evince", "neovim",
			"youtube-dl", "tmux", "cowsay", "update-grub", "xdg-desktop-portal-gtk", "polkit-gnome"
		],
		bspwm_packages=["xorg", "bspwm", "sxhkd", "xorg-xinit", "xclip", "feh", "lxappearance", "polybar", "xorg-xrandr", "xsettingsd"],
		hyprland_packages=["hyprland", "waybar", "swww", "cliphist", "wl-clipboard", "xdg-desktop-portal-hyprland", "qt5-wayland", "qt6-wayland"]
	),
	aur=DistributionPackages(
		common=[
			"gnome-calculator-gtk3", "flameshot-git", "rofi-lbonn-wayland-git", "bibata-cursor-theme", "tela-circle-icon-theme-dracula",
			"themix-theme-oomox-git", "themix-plugin-base16-git", "themix-icons-papirus-git", "themix-gui-git", "themix-export-spotify-git",
			"themix-theme-materia-git", "oomox-qt5-styleplugin-git", "oomox-qt6-styleplugin-git", "cava", "pokemon-colorscripts"
		],
		bspwm_packages=["i3lock-color", "picom-ftlabs-git"],
		hyprland_packages=["hyprpicker", "swaylock-effects-git", "wlr-randr-git"]
	)
)

CUSTOM = {
	"games": Packages(
		pacman=DistributionPackages(
			common=["steam", "gamemode", "mangohud"]
		),
		aur=DistributionPackages(
			common=["portproton"]
		)
	),
	"social_media": Packages(
		pacman=DistributionPackages(
			common=["telegram-desktop"]
		),
		aur=DistributionPackages(
			common=["vesktop"]
		)
	)
}
