from flask import Flask, render_template, url_for
from flask_weasyprint import HTML, render_pdf
import numpy as np
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/index.pdf')
def index_pdf():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=['student A','student B', 'student C'])
    df = df.append(df.agg(['sum', 'mean']))
    title = 'Score'
    html = render_template('index.html', title=title, now=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), table=df.to_html(classes='table table-bordered'))
    return render_pdf(HTML(string=html))
