# Kittens News
Web application for online news using Django.

Site specialized on the collecting and sharing of general news about kittens.

## How to test
```bash
cd kittens_news
```
```bash
python manage.py runserver or python3 manage.py runserver
```
```
Go to http://127.0.0.1:8000/ or http://localhost:8000/
```
## Work with
- Django start project and apps.
- Display news on different links from reading JSON file.
- Add news titles to homepage, grouped on dates and ordered by most recent ones.
- Add webpage that has a form for creating news from web using POST method.
- Update news every time user submits post, for not having to reload server when change is made.
- Generate random link for assign to news from 1000 to 9999 when these are created.
- Store actual time and date of posts created using datetime Python module, format 'AAAA-MM-DD HH:MM:SS'.
- JSON file is updated when a new post is created.
- Search bar form that sends GET requests to homepage for query specific words on news titles.

## Screenshots

### 1. Homepage

<img src="https://i.ibb.co/x89kfYF/c1.png" alt="c1">

### 2. Create post

<img src="https://i.ibb.co/rxWWWYx/c2.png" alt="c2">

### 3. Make query

<img src="https://i.ibb.co/TvqFJHh/c3.png" alt="c3">
  
### 4. News

<img src="https://i.ibb.co/SPdXpBv/c4.png" alt="c4">
