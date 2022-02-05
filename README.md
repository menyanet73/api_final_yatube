# Yatube API
### How start project:

Clone a repository and go to command line:

```
git clone git@github.com:menyanet73/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate virtual environment:

```
python3 -m venv env
```
For Windows:
```
source env/Scripts/activate  
```
For Linux:
```
source env/bin/activate  
```

Install dependencies from a file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Apply migrations:

```
python3 manage.py migrate
```

Start project:

```
python3 manage.py runserver
```