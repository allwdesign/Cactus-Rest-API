# Cactus-Rest-API

API provides the ability to record and receive information about cacti. API use TokenAuthentication and provide a mechanism for clients to obtain a token given the username and password.
[http://your_hostname/api-token-auth/](http://your_hostname/api-token-auth/)

API has a single entry point and  the browsable representation:  [http://your_hostname/api/v1/](http://your_hostname/api/v1/)

The docs provided by swager:  [http://your_hostname/docs/](http://your_hostname/api/v1/docs/)


## The following actions are available:

| Endpoint | Methods  | Actions  |Authenicated users and topics authors  |  Unauthenicated users  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| cacti | **GET** | The list of cacti | + | + |
| topics | **GET** | The list of topics about cacti | + | + |
| cacti/id | **GET** | Current cactus | + | + |
| topics/id | **GET** | Current topics | + | + |
| cacti / topics | **POST** | Make new cacti / topics  | + | - |
| cacti/id and topics/id | **PUT** | Editing the topics / information about cacti | + | - |
| cacti/id and topics/id | **DELETE** |  Deleting the topics / information about cacti | + | - |
