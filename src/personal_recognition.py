#!/usr/bin/env python3
import rospy
from theta_speech.srv import SpeechToText, SpeechToTextResponse
import rospkg
from std_msgs.msg import String
from std_msgs.msg import Empty
import time
from datetime import datetime
import unicodedata
import os


PACK_DIR = rospkg.RosPack().get_path("theta_personal_recognition_task")
LOG_DIR = os.path.join(PACK_DIR,"logs/")

tts_pub  = rospy.Publisher('/textToSpeech', String, queue_size=10)
face_pub = rospy.Publisher('/hri/affective_loop', String, queue_size=10)
detecion_pub = rospy.Publisher('/detection_activate', Empty, queue_size=10)
trainer_pub = rospy.Publisher('/trainer_activate', Empty, queue_size=10)


def log(text, log_name, print_text=False, show_time=True):
    now = datetime.now()

    with open(log_name, "a+") as log_file:
        log_text = now.strftime(f"[%H:%M:%S] {text}") if show_time else text
        log_file.write(f"{log_text}\n")

    if print_text:
        print(text)

def task_procedure(self):
    rospy.logwarn("Start")
    now = datetime.now()

    log_dir = os.path.join(PACK_DIR,"logs/")
    log_name = now.strftime("log_%H_%M_%S.txt")
    log_name = os.path.join(log_dir,log_name)

    log("Starting Personal Recognition", log_name)

    #Start
    tts_pub.publish('look at the camera and stay still...')
    face_pub.publish('littleHappy')
    time.sleep(1)
    
    #detection
    detecion_pub.publish()
    tts_pub.publish('Finish')
    time.sleep(1)
    face_pub.publish('happy')
    
    #depois que o bobão viro
    tts_pub.publish('Looking for my Operator...')
    time.sleep(1)
    trainer_pub.publish()
    tts_pub.publish('Ok, I found')


if __name__ == "__main__":  
    rospy.init_node("personal_recognition")
    rospy.Subscriber("hotword", Empty, task_procedure)
    rospy.Subscriber("face_detection_node", Empty, task_procedure)
    rospy.Subscriber("trainer_node", Empty, task_procedure)

    while not rospy.is_shutdown():
        pass