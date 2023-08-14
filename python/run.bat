@echo off

:: pip install -r requirements.txt
python -m geektrust sample_input\input1.txt
python -m geektrust sample_input\input2.txt
python -m unittest geektrust
coverage run -m unittest geektrust