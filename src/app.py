from flask import Flask, render_template, request, flash, redirect, url_for
from .scraper import scrape_df

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        distance = request.form['distance']
        if not title:
            flash('Title is required!')
        else:
            job_df = scrape_df(title, location, distance).set_index('Job Title')
            return render_template('job_posting.html',
                                tables=[job_df.to_html(classes='data')],
                                # header="true",
                                titles=job_df.columns.values)
    return render_template('get_job_postings.html')