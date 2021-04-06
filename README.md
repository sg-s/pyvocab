# vocab builder

A simple python vocabulary builder

## Usage


Within python:


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


