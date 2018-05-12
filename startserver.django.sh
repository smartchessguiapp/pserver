#!/bin/bash
chmod a+x lichess-bot/engines/stockfish-9-64
ls lichess-bot/engines -l
python simple.py "localhost" 3000 &
gunicorn gettingstarted.wsgi
