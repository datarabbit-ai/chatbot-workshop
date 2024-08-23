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

If you want to run additional content with huggingface - install required packages for it:

```
$ pip3 install -r requirements-hg.txt
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
$ pip3 install -r requirements-demo.txt
$ streamlit run app.py
```
