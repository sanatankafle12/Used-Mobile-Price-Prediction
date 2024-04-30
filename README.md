# minor_project
It is a simple eCommerce website that lets you valuate your phone, compare phones, and check if the pricing of a phone is reasonable.

## Process
  Scrapped Data From Websites Second hand market websites
  The data had many missing values that were cleaned
  
     Models For Validation
      1. Linear Regression - MAPE - 23%
      2. Gradient Boosting - MAPE - 14%
      3. Random Forest - MAPE - 9% [Chosen]
      
  KNN was Used for Recommendation
  UI was created using Django and js,HTML,css

https://github.com/sanatankafle12/minor_project/assets/42962016/53d2e3b5-7ec1-4cae-869d-9338fe43a64f

Link to the website:
- http://skafle239.pythonanywhere.com/

Run on your Machine
- clone the github repo
- setup virtual environment
- Install the required packages from requirements.txt
  ```pip install -r requirements.txt```
- run python manage.py runserver
