# ai-image-enhancer-web-app
This is a web application for image enhancement made using Django framework. It has various features implemented inside of it. Here is a list of few of them - 

1. User registration
2. User Login
3. Email verification through OTP
4. Color to B&W image
5. B&W to Color image
6. Upscale the resolution of image (Done using pre-made EDSR SuperRes model)
7. Administration (Pre-built inside Django)

This project is developed by Piyush C, Pushkar G, Shivam G.

---------------------------------------------------------------


Installing dependencies
-----------------------

To install all the dependencies inside the project directory use

**$ pip install -r requirements.txt**

or try creating a new environment. Use the name of enivronment which you want to create instead of 'env_name'.

**$ conda create --name env_name --file requirements.txt**

If in any case error occurs please install the dependencies manually.

Configuring Project (After cloning or downloading the repository)
-------------------

1. Inside the media folder create a empty folder named 'profile_pics'.

2. Inside the initial minipro directory paste the model https://drive.google.com/drive/folders/1RqVWQGeXuAcnF_uBjHnkOw01DfPQbPhE?usp=sharing download the entire model folder and paste it.

3. You will need to put your email, smtp, and email password inside the following files

       a) Inside the second minipro -> settings.py -> line no: 151-155

       b) Enhancer -> templates -> enhancer -> base.html -> line no: 23-27
       
       c) Users -> views.py -> line no: 15

4. In case any error occurs please refer official django documentation.

5. The admin username is my personal email id if you wish you can change or delete it.

6. Current admin credentials

       Username - Piyush
       Password - localhost@123

Screenshots
-----------

![image](https://user-images.githubusercontent.com/87484921/146679754-1e411ac1-3055-404d-8ac9-572409f7aff7.png)

![image](https://user-images.githubusercontent.com/87484921/146679778-59d8f412-f8e8-43de-9392-f00db890da8e.png)

![image](https://user-images.githubusercontent.com/87484921/146679797-705fd3f3-0408-4a30-b97f-346ad839777c.png)

![image](https://user-images.githubusercontent.com/87484921/146679810-f21574a7-d7df-448a-947b-491b80f183c8.png)




