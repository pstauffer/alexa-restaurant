# alexa-restaurant

## Description

Pick a restaurant!


## Installation

```
virtualenv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
python alexa-restaurant.py
```

## Configuration

### App
If you like another listen_ip or port, set the values in the `config.yml`

```
app_port: 5555
app_listen_ip: 0.0.0.0
```

### Customize Restaurants
Create a `template.yml` file and add these key entries with your values.

```
---
bye_msg: Okay schade... bye

welcome_msg: Hallo Raiffeisen, soll ich euch sagen, wohin wir essen gehen?

answer_msg: Wir gehen

start_msg: Restaurant picker läuft

restaurants:
  - in den Schwanen
  - ins Armenhaus
  - in die Tschiardino
  - zum Gas-Heini
  - über die Gasse
  - zur Taverna
  - ins Gentile
  - zum Bierfalken
  - zum Veccia Posta
```
