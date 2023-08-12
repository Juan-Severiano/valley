# Instalar e configurar ZSH
```bash
sudo apt install zsh -y
chsh -s /bin/zsh
zsh
```
# Instalar Oh-my-zsh! -> https://ohmyz.sh/
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

# Instalar Spaceship Prompt
# https://github.com/spaceship-prompt/spaceship-prompt

```bash
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
```

# Mudar ~/.zshrc -> ZSH_THEME="spaceship"

# Instalar Zsh Autosuggestions
# https://github.com/zsh-users/zsh-autosuggestions

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

# Instalar Zsh Syntax Highlighting
# https://github.com/zsh-users/zsh-syntax-highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

# Mudar plugins
# plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# Font optional (https://github.com/pdf/ubuntu-mono-powerline-ttf)
```bash
mkdir -p ~/.fonts
git clone https://github.com/pdf/ubuntu-mono-powerline-ttf.git ~/.fonts/ubuntu-mono-powerline-ttf
fc-cache -vf
```

# REBOOT!!!!!!!!!!!!!!!!!!!!!
