FROM archlinux:latest

RUN pacman -Syyu --noconfirm && pacman -S python uv python-pipx zsh sudo git ffmpeg base-devel cmake neovim pkgconf texlive --noconfirm

RUN useradd -m dev
RUN printf 'dev145\ndev145\n' | passwd dev
RUN echo 'dev ALL=(ALL:ALL) ALL' >> /etc/sudoers

WORKDIR /home/dev/

USER dev
RUN printf '\ndev145\n' | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pipx install manim

RUN echo 'export PATH="$PATH:$HOME/.local/bin"' >> $HOME/.zshrc

CMD ["zsh"]