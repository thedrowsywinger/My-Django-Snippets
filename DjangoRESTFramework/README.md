# My Django Snippets 

## Django REST Framework 

 

In this snippet , I plan to implement simple REST API functions in Django.  

 

##### Simple REST API communication  

 

This is a simple way of sending certain info with the API, verifying the information. 

 

## Installation  

 

There is a requirements.txt file included for installing all the dependencies.  

 

```sh 
cd DjangoRESTFramework 
pip install -r requirements.txt 
``` 

 

For using the REST API, one must do the following:  

 

```sh 
python manage.py makemigrations 
python manage.py migrate 
python manage.py run server 
``` 

 

Then in the postman window, we can use the following link: http://127.0.0.1:8000/ 

N.B: IT must be a POST request  

You can also make a GET request with the same link  

 