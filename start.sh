if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/VysakhTG/Eva-Mod.git /Eva-Mod
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Eva-Mod
fi
cd /Eva-Mod
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
