# Harnessing GenAI power with your own custom chatbot @ PyConPL 2024

Generative AI is a very hot topic nowadays. And rightfully so, as with the recent developments in the area, quite a 
lot of new business applications have been enabled or made significantly easier in the implementation. AI is currently 
also getting more accessible than ever, with some models becoming small enough to run on one personal device
while remaining quite capable, or with all 3rd party models APIs (such as OpenAI’s) available.

During this workshop, we will take advantage of that fact (as well as APIs making these
models accessible) to start the adventure with generative AI, and build our own chatbot/assistant with conversational
capabilities and the ability to interact with custom data.

Workshop brought to you by [datarabbit.ai](https://datarabbit.ai).

# Preliminary requirements
- Python is installed on your machine, preferably in version 3.10 (this is the oldest version that we tested on).
- There will be some API keys required for the workshop – please refer to the notebook initial sections for details.

# How to set up the workshop environment

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

Start a Jupyter server...

```
$ jupyter lab .
```

... go to the notebook `workshop.ipynb`!

`workshop_solutions.ipynb` is the copy of the notebook – but with reference solutions to the exercises.

## Starting demo chatbot app

create file `.streamlit/secrets.toml` with content:

```
OPENAI_API_KEY = "YOUR_API_KEY"
```

run from terminal:

```
$ pip3 install -r requirements-demo.txt
$ streamlit run app.py
```


## Contact
If you tried out the configuration or actual tutorials prior to the workshop, after it ended, or you strolled here from
the Internet and when working with the materials you encountered some issues, or perhaps you would like to implement 
some more advanced chatbot project and would need help - feel free to
[contact us](mailto:kamil.sagalara@datarabbit.ai,michal.mikolajczak@datarabbit.ai,wiktor.smura@datarabbit.ai).
