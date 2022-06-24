# Arrival Test Framwork

## Info

- There are [bugs descriptions](./bugs.md)
- There are [cases descriptions](./cases.md)
- didn't have time for pretify enums of `signals` and `pins`, but as is.. sory for harcode ^^

## Get Started
After clone the repo, paste inside a folder

```bash
python3 -m venv venv && source venv/bin/activate && pip install -U -r requirements.txt
```

## Launch

Run first the smoke suite

```bash
python -m pytest -s -vv -k e2e/smoke/
```

or special cases only

```bash
python -m pytest -s -vv -k e2e/cases/
```

or just... ti run all tests

```bash
python -m pytest -s -vv
```
