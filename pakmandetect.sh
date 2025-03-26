#!/usr/bin/env bash
for pm in apk app apt apt-get cargo dnf dpkg emerge eopkg flatpak nala moss nix-env pacman pamac portage rpm snap xbps yay yum zypper; do
    echo | command -v $pm
done
exit 0