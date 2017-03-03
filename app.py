from flask import Flask
from flask_ask import Ask, statement, question
import yaml
import sys
from random import randint


def yml_loader(file):
    try:
        with open(file, 'r') as stream:
            return yaml.load(stream)
    except IOError:
        sys.exit(1)


template = yml_loader('template.yml')

app = Flask(__name__)
ask = Ask(app, '/')


def get_restaurant():
    restaurants = template['restaurants']
    rand = randint(0, len(restaurants) - 1)
    return restaurants[rand]


@app.route('/')
def homepage():
    homepage = template['start_msg']
    return homepage


@ask.launch
def start_skill():
    welcome_msg = template['welcome_msg']
    return question(welcome_msg)


@ask.intent('AMAZON.YesIntent')
@ask.intent('YesIntent')
def yes_intent():
    restaurant = get_restaurant()
    return statement(template['answer_msg'] + ' ' + restaurant)


@ask.intent('AMAZON.NoIntent')
def no_intent():
    bye_text = template['bye_msg']
    return statement(bye_text)


@ask.intent('AMAZON.StopIntent')
def stop_intent():
    bye_text = template['bye_msg']
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel_intent():
    bye_text = template['bye_msg']
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
