FROM archlinux:latest

RUN pacman -Syyuu --noconfirm && pacman -S git python python-pipx uv --noconfirm
