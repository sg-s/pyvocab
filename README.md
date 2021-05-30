# vocab builder

A simple python vocabulary builder

## Usage


The recommended way of using this is within [Jupyter Lab](https://jupyter.org/install). Once you have that installed, import it using:

```python
from pyvocab import vocab
```




### Read all words in the dictionary

```python
words = vocab.read()
```

### Lookup all words using a dictionary service, and save definitions

```python
vocab.lookup()
```

### Interactive test

```python
vocab.test()
```


### Scrape /r/logophilia for new words

First, create two files called `.clientid` and `.clientsecret` with your reddit bot clientID and client secret. Then:

```python
vocab.reddit()
```


## Developing

If you are developing this, you probably want to make your life a little easier. Before importing `pyvocab`, 

```python
%load_ext autoreload
%autoreload 2

```

