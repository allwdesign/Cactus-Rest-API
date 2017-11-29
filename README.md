# Cactus-Rest-API
API provides the ability to record and receive information about cacti

API has a single entry point and  the browsable representation: 
http://<your hostname>/

API has a docs provided by swager: 
http://<your hostname>/docs/

Use Admin part for creating users.
http://<your hostname>/admin/

API use TokenAuthentication and provide a mechanism for clients to obtain a token given the username and password.
http://<your hostname>/api-token-auth/

For authenticated users and article authors about cacti, the following actions are available:

1.viewing the list of cacti(GET)
http://<your hostname>/cacti/

2.viewing the list of articles about cacti(GET)
http://<your hostname>/topics/

3.viewing current cactus(GET)
http://<your hostname>/cacti/<id>

4.viewing current topics(GET)
http://<your hostname>/topics/<id>

5.make new cacti/articles(POST)

6.editing the articles / information about cacti(PUT)

http://<your hostname>/cacti/<id>
http://<your hostname>/topics/<id>

7.deleting the articles / information about cacti(DELETE)

http://<your hostname>/cacti/<id>
http://<your hostname>/topics/<id>

For  unauthenticated users or not owner provides the following actions:

1.viewing the list of cacti(GET)
http://<your hostname>/cacti/

2.viewing the list of articles about cacti(GET)
http://<your hostname>/topics/

3.viewing current cactus(GET)
http://<your hostname>/cacti/<id>

4.viewing current topics(GET)
http://<your hostname>/topics/<id>
