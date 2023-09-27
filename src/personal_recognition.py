#!/usr/bin/env python3
import rospy
from theta_speech.srv import SpeechToText, SpeechToTextResponse
import rospkg
from std_msgs.msg import String, Empty
import time
from datetime import datetime
import os

PACK_DIR = rospkg.RosPack().get_path("theta_personal_recognition_task")

tts_pub  = rospy.Publisher('/textToSpeech', String, queue_size=10)
face_pub = rospy.Publisher('/hri/affective_loop', String, queue_size=10)
operador_detection = rospy.Publisher('/face_detection/operador_take', Empty, queue_size=10)
comparador_detection = rospy.Publisher('/face_detection/comparador_take', Empty, queue_size=10)
recognition_run = rospy.Publisher('/face_detection/recognition', Empty, queue_size=10 )

def task_procedure(self):
    rospy.logwarn("Start")
    face_pub.publish('littleHappy')

    tts_pub.publish('look at the camera and stay still')
    time.sleep(3)
    operador_detection.publish()
    time.sleep(3)
    tts_pub.publish('Finish')
    face_pub.publish('happy')
    time.sleep(1)
    
    #depois que o bobão viro
    tts_pub.publish('Looking for my Operator...')
    time.sleep(3)
    comparador_detection.publish()
    time.sleep(3)
    recognition_run.publish()
    tts_pub.publish('Ok, I found')

if __name__ == "__main__":  
    rospy.init_node("personal_recognition")
    rospy.Subscriber("hotword", Empty, task_procedure)
    rospy.Subscriber("face_detection_node", Empty, task_procedure)
    rospy.Subscriber("trainer_node", Empty, task_procedure)

    while not rospy.is_shutdown():
        pass