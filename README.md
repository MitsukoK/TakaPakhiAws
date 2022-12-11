Taka pakhi API user GUIDE

### 1. Login User (POST)

http://54.226.160.184/user/login/

#### Request

within the **body** of the request, you need to send the following data:

  * userphone/name
  * password

{
    "username": "01991896271",
    "password": "popcorn1234"
}

#### Response

  * 200: OK
  * {
    "token": "45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }

### 2. Logout User (POST)

url -> http://54.226.160.184/user/logout/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }

#### Response
    
      * 200: OK
      * _it will delete the token from the database_

### 3. Get User Mobile Banking (GET)

url -> http://54.226.160.184/user/mobile_bank/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * [{"mobile_banking":["Mkash"]}]

### 4. Get User Banking (GET)

url -> http://54.226.160.184/user/bank/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * [{"bank":["Asia Bank"]}]

### 5. Get User Mobile Recharge (GET)

url -> http://54.226.160.184/user/recharge/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * [{"mobile_recharge":["Banglalink"]}]


### 6. User Current Balance (GET)
url -> http://54.226.160.184/user/current_balance/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * int(23432) _Note: this integer is the user current balance_
  

### 7 (a). User Banking Transaction History (GET)

url -> http://54.226.160.184/request/banking/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * Response type List:Map<String,dynamic>
    * [
        {
            "id": 1,
            "amount": 1000,
            "bank_name": "Asia Bank",
            "bank_account_number": "1234567890",
            "bank_account_name": "Burhan Uddin",
            "branch_name": "Dhanmondi",
            "is_term": true,
            "created_at": "2022-11-29T11:30:52.196693Z",
            "status": "Pending"
        }
    ]


### 7 (b). User Banking Transaction Request (Post)

url -> http://54.226.160.184/request/banking/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
    within the **body** of the request, you need to send the following data in json format:
    ```
    {
        "amount": 1000,
        "bank_name": "Asia Bank",
        "bank_account_number": "1234567890",
        "bank_account_name": "Burhan Uddin",
        "branch_name": "Dhanmondi",
        "is_term": true // is term and condition accepted or not
    }
    ```
#### Response
    * 200: OK
    * Response type List:Map<String,dynamic>
    * The transaction is successful {
        "id": 1,
        "amount": 1000,
        "bank_name": "Asia Bank",
        "bank_account_number": "1234567890",
        "bank_account_name": "Burhan Uddin",
        "branch_name": "Dhanmondi",
        "is_term": true,
        "created_at": "2022-11-29T11:30:52.196693Z",
        "status": "Pending"
    }

### 8 (a). User Mobile Banking Transaction History (GET)

url -> http://54.226.160.184/request/mobilebanking/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token 45770da46ab8c4b22d33d306cc9fe7c04babe2a8"
    }
#### Response
    * 200: OK
    * Response type List:Map<String,dynamic>
    * [
        {
            "id": 1,
            "amount": 1000,
            "phone_number": "01991896271",
            "bank_name": "Mkash",
            "choice": "Personal",
            "is_term": true,
            "created_at": "2022-11-29T11:47:30.901206Z",
            "status": "Pending"
        }
    ]

### 8 (b). User Mobile Banking Transaction Request (Post)

url -> http://54.226.160.184/request/mobilebanking/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token
    }
    within the **body** of the request, you need to send the following data in json format:
    ```
    {
        "amount": 1000,
        "phone_number": "01991896271",
        "bank_name": "Mkash",
        "choice": "Personal", // Personal or Agent
        "is_term": true 
    }
    ```
#### Response
    * 200: OK
    * The transaction is successful {
        "id": 1,
        "amount": 1000,
        "phone_number": "01991896271",
        "bank_name": "Mkash",
        "choice": "Personal",
        "is_term": true,
        "created_at": "2022-11-29T11:47:30.901206Z",
        "status": "Pending"
    }   

### 9 (a). User Mobile Recharge Transaction History (GET)

url -> http://54.226.160.184/request/mobilercharge/

#### Request 
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token
    }
#### Response
    * 200: OK
    * Response type List:Map<String,dynamic>
    * [
        {
            "id": 1,
            "amount": 1000,
            "phone_number": "01991896271",
            "choice": "Prepaid",
            "is_term": true,
            "created_at": "2022-11-29T11:53:21.365865Z",
            "status": "Pending"
        }
]

### 9 (b). User Mobile Recharge Transaction Request (Post)

url -> http://54.226.160.184/request/mobilercharge/

#### Request
    you need pass the Authorization token in the headers of the request
    {
        "Authorization":"token
    }
    within the **body** of the request, you need to send the following data in json format:
    ```
    {
        "amount": 1000,
        "phone_number": "01991896271",
        "choice": "Prepaid", // Prepaid or Postpaid
        "is_term": true 
    }
    ```
#### Response
    * 200: OK
    * The transaction is successful {
        "id": 1,
        "amount": 1000,
        "phone_number": "01991896271",
        "choice": "Prepaid",
        "is_term": true,
        "created_at": "2022-11-29T11:53:21.365865Z",
        "status": "Pending"
    }