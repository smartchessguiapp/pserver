#!/bin/bash
chmod a+x lichess-bot/engines/stockfish-9-64
ls lichess-bot/engines -l
python simple.py "" $PORT
