#### clone the repo

```bash
    git clone https://github.com/booringreader/web-crawler.git
    cd web-crawler
```

#### Execute
1. if the existing one doesn't work, remove ```venv``` dir & create a new virtual environment with
```bash
python -m venv venv # macOS/Linux
```
2. install dependencies with
```bash
pip install beautifulsoup4
```
3. execute the ```urls.py``` file first, then enter the root url(the first page, the entry point); this will populate the ```urls.csv``` file
4. execute the ```mails.py``` file
