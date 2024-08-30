import naoqi
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "10.60.9.16", 9559)
tts.say("Hello world, from group 4")
