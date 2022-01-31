TPU accelerated Rasperrypi Aimbot

This project was made to expose that an object detection aimbot can run on a raspberry pi.

to get tfobject detection to work on Raspi follow this guide
https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md

then run this file inside of the environment above Testing/ShootEnemy.py

you will need a Arduino leonardo to run the .ino sketch

if you want to quantize a tf2 modal use
script for quantizing Modals for tpu eceleration is in Quant_Script.ipynb


Note:

that I will not be sharing any modals that I end up training for this project, becuse I do not want them to be used to cheat. I have provided the script that I used
to quantize the Tensor Flow graphs becuse it has alot of other uses beyond this aimbot.

![image](https://user-images.githubusercontent.com/84061212/128445701-0983c2fa-cfbb-4f09-8971-62a897320144.png)

For this project you will need and arduino micro, a google coral edge TPU a raspberry Pi and a HDMI to CSI2 adapter. 

![image](https://user-images.githubusercontent.com/84061212/128445781-20273b06-7070-4073-a00b-309a82efd0be.png)



