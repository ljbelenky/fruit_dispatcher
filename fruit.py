import numpy as np
from numpy.random import choice, randint
import pandas as pd 

from flask import Flask, render_template, request, url_for
import json

n = 100

fruit = ['apple','orange','banana','mango','pear']
quality = ['poor','fair','average','good','excellent', np.nan]
condition = ['unripe','ripe','overripe','rotten']
style = ['fancy','regular', np.nan]
weight_ounces = (2, 10)
packaging = [True, False, np.nan]
start_date = pd.Series(pd.date_range('2020-01-01', '2020-12-31', n)).sample(n, replace = True)
end_date = start_date + choice(pd.timedelta_range('1 day', periods = n), n)

start_date = start_date.dt.strftime('%Y-%m-%d')
end_date = end_date.dt.strftime('%Y-%m-%d')



fruits = pd.DataFrame({'type':choice(fruit, n),
                        'quality': choice(quality, n),
                        'weight': randint(*weight_ounces, n),
                        'condition': choice(condition, n),
                        'style': choice(style, n),
                        'packaging': choice(packaging, n),
                        'start_date': start_date,
                        'end_date': end_date
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