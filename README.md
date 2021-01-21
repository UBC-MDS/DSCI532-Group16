# Mental Health Awareness Dashboard

![app sketch](images/app_sketch_v1.png)

The app is a dashboard to more efficiently consume the mental illness survey data and drive insights into different areas of mental illness awareness in tech companies around the world. After landing on this dashboard, users can filter generic company, employee and mental health related filters on the left hand side. For example, they can filter by region and age group. The filtering will then drive the visualizations on the tabbed right side of the app.

Each tab will then answer specific topics that our target audience might be interested in. For example, the tabs could include:
- Awareness (of mental illness)
- Healthcare Benefits (vs mental illness)
- Privacy (around mental illness)

Within each tab, we may include different visualizations that will tell a story around each topic. For example, the user may try to understand mental illness awareness by state by going to the Awareness tab and then toggling different states in the US.


## Usage

There are two suggested ways to run this analysis:

### 1. Deploy and run on Heroku

This dashboard is hosted on Heroku: https://it-mental-health-dash.herokuapp.com/ 
The heroku repository URL is: https://git.heroku.com/it-mental-health-dash.git

#### Deploy on to your own Heroku Account
Once you've cloned this github repository, you can do the following from the root of the repo:
```bash
heroku create [app_name]
git push heroku main
heroku ps:scale web=1
```
#### If you make changes and want to redeply to Heroku
Note this does not include details on fork and branch handling in github.
```bash
git status
git add .
git commit -m "change description"
git push heroku main
heroku ps:scale web=1
```
### 2. Run without Heroku

After cloning this repository and installing the python dependencies below, run the following from the root of this repo:

```bash
python src/app.py
```


## Dependencies

### Python

We are providing you with a `pip` environment file which is available [here](requirements.txt). You can download this file and install dependencies in your desired environment.

```
pip install -r requirements.txt
```

```
pandas
gunicorn
altair
dash==1.18.1
dash_bootstrap_components
plotly==4.14.3
vega_datasets
```


