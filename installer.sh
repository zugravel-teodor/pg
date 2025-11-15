mkdir -p ~/.config/pg
cp main.py ~/.config/pg/main.py
echo 'alias pg="python3 ~/.config/pg/main.py"' >> ~/.bashrc
source ~/.bashrc