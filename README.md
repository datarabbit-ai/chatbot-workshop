# How to set up the workshop?

Create virtual environment

```
$ python3 -m venv venv
```

Activate it

```
$ source venv/bin/activate
```

Install required packages

```
$ pip3 install -r requirements.txt
```

Start a notebook

```
$ jupyter lab .
```

## Starting demo

create file `.streamlit/secrets.toml` with content:

```
OPENAI_API_KEY = "YOUR_API_KEY"
```

run from terminal:

```
streamlit run app.py
```
