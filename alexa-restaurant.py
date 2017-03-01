from flask import Flask
from flask_ask import Ask, statement, question
import yaml
import sys
from random import randint


app = Flask(__name__)
ask = Ask(app, '/')


def get_restaurant():
    restaurants = config['restaurants']
    rand = randint(0, len(restaurants) - 1)
    return restaurants[rand]


@app.route('/')
def homepage():
    homepage = config['homepage']
    return homepage


@ask.launch
def start_skill():
    welcome_msg = config['welcome']
    return question(welcome_msg)


@ask.intent('AMAZON.YesIntent')
@ask.intent('YesIntent')
def yes_intent():
    restaurant = get_restaurant()
    return statement(config['answer'] + ' ' + restaurant)


@ask.intent('AMAZON.NoIntent')
def no_intent():
    bye_text = config['bye']
    return statement(bye_text)


@ask.intent('AMAZON.StopIntent')
def stop_intent():
    bye_text = config['bye']
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel_intent():
    bye_text = config['bye']
    return statement(bye_text)


if __name__ == '__main__':

    try:
        with open('config.yml', 'r') as stream:
            config = yaml.load(stream)
    except IOError as err:
        sys.exit(1)

    app.run(debug=True, host=config['app_listen_ip'], port=config['app_port'])
