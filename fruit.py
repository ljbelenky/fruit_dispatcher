import numpy as np
from numpy.random import choice, randint
import pandas as pd 

from flask import Flask, render_template, request, url_for
import json

fruit = ['apple','orange','banana','mango','pear']
quality = ['poor','fair','average','good','excellent']
condition = ['unripe','ripe','overripe','rotten']
style = ['fancy','regular', np.nan]
weight_ounces = (2, 10)
packaging = [True, False, np.nan]

n = 100

fruits = pd.DataFrame({'type':choice(fruit, n),
                        'quality': choice(quality, n),
                        'weight': randint(*weight_ounces, n),
                        'condition': choice(condition, n),
                        'style': choice(style, n),
                        'packaging': choice(packaging, n)
                        })


app = Flask(__name__)

@app.route('/')
def home():
    data = fruits.sample().values[0]
    data = {k:v for k,v in zip(fruits.columns, data)}
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000, debug = True)

print(fruits.head())