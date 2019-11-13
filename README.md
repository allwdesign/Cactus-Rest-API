# Cactus-Rest-API

API provides the ability to record and receive information about cacti. API use TokenAuthentication and provide a mechanism for clients to obtain a token given the username and password.
[Link](http://your_hostname/api-token-auth/)

API has a single entry point and  the browsable representation:  http://your_hostname/

The docs provided by swager:  http://your_hostname/docs/


## The following actions are available:

| Methods  | Actions  |Authenicated users and topics authors  |  Unauthenicated users  |
| ------------ | ------------ | ------------ | ------------ |
| **GET** | The list of cacti  http://your_hostname/cacti/ | + | + |
| **GET** | The list of topics about cacti  http://your_hostname/topics/  | + | + |
| **GET** | Current cactus  http://your_hostname/cacti/id  | + | + |
| **GET** | Current topics  http://your_hostname/topics/id  | + | + |
| **POST** | Make new cacti / topics  | + | - |
| **PUT** | Editing the topics / information about cacti  http://your_hostname/cacti/id http://your_hostname/topics/id  | + | - |
| **DELETE** |  Deleting the topics / information about cacti http://your_hostname/cacti/id http://your_hostname/topics/id | + | - |
