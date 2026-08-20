# open source

the intended software is to be free to use to help users own a bot that posts nostalgic gaming clips to discord every 2 weeks for personal or groupchat use.

# tech stack

Python - programming langugage
FastAPI - backend framework
Discord.py - discord client
Nvidia API - optional API for clip captioning
AWS - cloud provider to store clips 


## setup

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## usage

put a `.env` file in the root with your keys, put videos in `videos/`, then run it.

## structure

```
app/serives/    business logic
requirements.txt
```

## license

MIT