# deaf-aid

## Abstract

#### This project was initially made to help deaf people and normal people to communicate with each other using a small device based on Raspberry pi
#### The projects idea was split into two, the first one is understanding the voice of the normal human being and translate it as text for the deaf person.
#### the second was taking the deaf person's hand gestures and translate it into voice or even text for the normal human being to understand.
#### The first part of the project was does successfully but the second part wasn't completed as the project changed at that time into another project
#### but mainly for the second part we had three ideas one using mediapipe library to make it easy and the second was using deep learning to make it more effective and accurate, both neeeded a camera to take the gestures and a speaker to speak or even take the text on the same LCD.
#### The third idea was to take the hand gestures of the deaf person by making him wear a glove that had flexable resistors, this way we could take the inputs as variable values of the resistors and that would have made it much cheaper.

#### however i'll talk about the first part as it was the one that was finished .
## **Main Components**

#### RaspberryPi , 16x2 Character LCD, Microphone, Power source, Internet source.

#### The following image will give you a glimpse  of the hardware connections
![img](https://github.com/ENG-MohamedEssam/deaf-aid/blob/main/images/img.png)
#### The raspberry pi was used as the main processor, the microphone took the voice of the normal human being, then the raspberry pi would process the voice data and recognize it then display it on the LCD 
#### The following two codes were the main codes that were used for the project
####[input-audio](https://github.com/ENG-MohamedEssam/deaf-aid/blob/main/Speech_Recognition_Test.py)
####[output-text](https://github.com/ENG-MohamedEssam/deaf-aid/blob/main/LCD_PYTHON.py)
#### also the codes went throught a lot of modification, such as the following code was some kind of LCD driver but to make it easier i used an already made driver in the final code
####[old-lcd-driver](https://github.com/ENG-MohamedEssam/deaf-aid/blob/main/LCD_PYTHON_OLD.py)
#### So to make the Raspberry pi run the codes on the startup i used the following script to make it launch it while starting up
####[script](https://github.com/ENG-MohamedEssam/deaf-aid/blob/main/launcher.sh)
#### you will find a video explanation in the following link for the whole project
#### for the power source at first i was using the phone's charger but for the final product i planned to use lipo battery or a power bank 
#### for the internet source i used the phone's usb using usb tethering method but for the final product i planned to use usb dongle or offline voice recognition library 
####[Explanation](https://drive.google.com/drive/u/0/folders/1KUh7kfPaU8bGa7THwe2R01-4G6Q_rnNO)