# Google-calendar-add-event

##  How to Create a project in Google Developer Console?

To kick things off lets head [Google Developers Console] (https://console.developers.google.com/) and create a new project. We name the project as Automating Calendar.

![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/2.jpg)

Then go to the dashboard and search for Calendar API in the search bar in order to enable the Calendar API for your project.

![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/3.jpg)
![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/4.jpg)
![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/5.jpg)

The first step is done. We need to now, move over to generate credentials which will be used.

## How to generate application credentials for Google Calendar API?

The first thing to do is to go to the OAuth Consent Screen tab, provide it an application name, pick all the necessary scopes that you would like to obtain permissions for. For instance, if you need only read permissions or edit, specify the checkboxes as per your need.

![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/6.jpg)
![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/7.jpg)


Once the application scope and consent screen is setup, we proceed to generating the credentials. On the credentials tab, click the Create credentials, and then select the OAuth client ID, specify the major platform where you will be using the applicatin, if you are not sure, select the Other box. This generates the Client ID and Client Secret Keys but we want them as in a JSON file so download and save the file. We will need this in next step.

![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/8.jpg)
![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/9.jpg)
![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/10.jpg)

Find the downloaded file and rename it as credentials.json, save it preferably in the same directory, where you will start writing your code.

![image](https://karenapp.io/articles/images/Google-Blogs/gcalautomation/11.jpg)

### Thanks [Keran.io](https://karenapp.io/) for the detailed explanation. [Source](https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/)