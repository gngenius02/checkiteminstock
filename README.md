# checkiteminstock

### Descrition
  Check a site for in stock products.

### Requirements

- Python3 installed
- gmail account with an app password activated.
- yagmail installed through pip, check perpartion.

### Preparation

- go to 'https://myaccount.google.com/apppasswords' and setup an app password if you haven't already. ( You will need this to send emails ).
- install yagmail package with: 
  ```shell 
  pip install yagmail
  ```
- update the files links.txt and creds.txt with your infomation.
- run the following to start:
  ```shell
  python3 gotime.py
  ```

 # Example output to shell
 
  ```shell
  checking url https://www.example.com/product/secretprodut0/
  not in stock moving on
  not in stock moving on
  checking url https://www.example.com/product/secretproduct1/
  in stock sending email
  ```
