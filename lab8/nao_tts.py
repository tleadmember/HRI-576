import time
import naoqi
import math
from naoqi import ALProxy

# tts = ALProxy

ip = "10.60.253.210"  # ADJUST MANUALLY !!!

# text to speech proxy
tts = ALProxy("ALTextToSpeech", ip, 9559)
tts.setParameter("speed", 92)

audo = ALProxy("ALAudioDevice", ip, 9559)
audo.setOutputVolume(70)
# 10.60.253.210
# animated speech proxy
animated_speech = ALProxy("ALAnimatedSpeech", ip, 9559)

# posture proxy
posture_proxy = ALProxy("ALRobotPosture", ip, 9559)

current_posture = posture_proxy.getPosture()

# gaze-related proxies
# awareness_proxy = ALProxy("ALBasicAwareness", ip, 9559)
# awareness_proxy.setEngagementMode("FullyEngaged")
# awareness_proxy.setEnabled(True)
# awareness_proxy.setStimulusDetectionEnabled("Touch", True)

# gaze-related proxies
tracker_proxy = ALProxy("ALTracker", ip, 9559)

text_old = ""


# motion proxy
motion_proxy = ALProxy("ALMotion", ip, 9559)
motion_proxy.wbEnable(True)


# Function to convert degrees to radians
def deg_to_rad(deg):
    return deg * math.pi / 180


right_arm_joints = [
    "RShoulderPitch",
    "RShoulderRoll",
    "RElbowYaw",
    "RElbowRoll",
    "RWristYaw",
    "RHand",
]

left_arm_joints = [
    "LShoulderPitch",
    "LShoulderRoll",
    "LElbowYaw",
    "LElbowRoll",
    "LWristYaw",
    "LHand",
]


def thumbs_up_motion():
    right_arm_angles_degrees_thumbs_up = [37.7, 8.4, 84.2, 41.8, -0.4, 0.02]
    right_arm_angles_radians_thumbs_up = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_thumbs_up
    ]
    left_arm_angles_degrees_thumbs_up = [35.0, -6.7, -94.0, -38.3, 7.2, 0.02]
    # left_arm_angles_degrees_thumbs_up = [37.7, -8.4, -84.2, -41.8, 4.4, 0.02]

    left_arm_angles_radians_thumbs_up = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_thumbs_up
    ]

    fractionMaxSpeed = 0.35
    joints = left_arm_joints + right_arm_joints
    angles_radians_thumbs_up = (
        left_arm_angles_radians_thumbs_up + right_arm_angles_radians_thumbs_up
    )

    motion_proxy.setAngles(joints, angles_radians_thumbs_up, fractionMaxSpeed)

    time.sleep(1.0)


def hips_motion():
    right_arm_angles_degrees_hips = [112.7, -43.2, 30.2, 86.0, -11.6, 0.02]
    right_arm_angles_radians_hips = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_hips
    ]
    left_arm_angles_degrees_hips = [84.5, 39.2, 6.1, -83.8, -9.5, 0.02]
    left_arm_angles_radians_hips = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_hips
    ]

    fractionMaxSpeed = 0.2
    joints = left_arm_joints + right_arm_joints
    angles_radians_hips = left_arm_angles_radians_hips + right_arm_angles_radians_hips

    motion_proxy.setAngles(joints, angles_radians_hips, fractionMaxSpeed)
    time.sleep(1.3)


# Flex motion
def flex_motion():
    right_arm_angles_degrees_flex = [-4.6, -68.6, 86.7, 88.5, 75.4, 0.0]
    right_arm_angles_radians_flex = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_flex
    ]
    left_arm_angles_degrees_flex = [-8.8, 70.0, -75.1, -87.6, -72.0, 0.02]
    left_arm_angles_radians_flex = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_flex
    ]

    fractionMaxSpeed = 0.2
    joints = left_arm_joints + right_arm_joints
    angles_radians_flex = left_arm_angles_radians_flex + right_arm_angles_radians_flex

    motion_proxy.setAngles(joints, angles_radians_flex, fractionMaxSpeed)
    time.sleep(1.0)


def zero_motion():

    right_arm_angles_degrees_zero = [85.1, -12.7, 67.4, 22.6, 7.1, 0.5]
    right_arm_angles_radians_zero = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_zero
    ]
    left_arm_angles_degrees_zero = [82.9, 11.9, -70.1, -23.2, 4.2, 0.5]
    left_arm_angles_radians_zero = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_zero
    ]

    fractionMaxSpeed = 0.2
    joints = left_arm_joints + right_arm_joints
    angles_radians_zero = left_arm_angles_radians_zero + right_arm_angles_radians_zero

    motion_proxy.setAngles(joints, angles_radians_zero, fractionMaxSpeed)
    time.sleep(1.0)


def sleep_action(dur):
    time.sleep(dur)


script2 = [
    "Hello Friend! My name is Mentor, and I'm your coach today.",
    "<sleep,0.1>",
    "For today's exercise, we're going to do an affirmation together.",
    "<sleep,0.2>",
    "Don't worry! I'll explain how it works before we begin.",
    "<sleep,0.1>",
    "Here's what we do",
    "<sleep,0.1>",
    "First, we flex our arms over our heads like this",
    "<flex>",
    "and we say, I am STRONG!",
    "<sleep,0.2>",
    "Then, we put our hands on our hips like this",
    "<hips>",
    "and we say, I am BRAVE!",
    "<sleep,0.2>",
    "Then, we give two thumbs up like this",
    "<thumbs_up>",
    "and we say, I can DO THIS!",
    "<sleep,0.2>",
    "<zero>",
    "So, the whole affirmation goes",
    "<flex>",
    "I am STRONG!",
    "<sleep,0.2>",
    "<hips>",
    "I am BRAVE!",
    "<sleep,0.2>",
    "<thumbs_up>",
    "I can DO THIS!",
    "<sleep,0.2>",
    "<zero>",
    "OK, now let's do it together. Are you ready?",
    "<sleep,1.0>",
    "Here we go...",
    "<flex>",
    "I am STRONG!",
    "<sleep,0.2>",
    "<hips>",
    "I am BRAVE!",
    "<sleep,0.2>",
    "<thumbs_up>",
    "I can DO THIS!",
    "<sleep,0.2>",
    "<zero>",
    "Great job! Thanks for doing the affirmation with me.",
    "<sleep,0.1>",
    "That's all for today!",
]


script3 = [
    "Hello Friend! My name is Mentor, and I'm your coach today.",
    "<sleep,0.1>",
    "For today's exercise, we're going to do an affirmation together.",
    "<sleep,0.2>",
    "Don't worry! I'll explain how it works before we begin.",
    "<sleep,0.1>",
    "Here's what we do",
    "<sleep,0.1>",
    "First, we flex our arms over our head",
    "and we say, I am STRONG!",
    "<sleep,0.2>",
    "Then, we put our hands on our hips",
    "and we say, I am BRAVE!",
    "<sleep,0.2>",
    "Then, we give two thumbs up",
    "and we say, I can DO THIS!",
    "<sleep,0.2>",
    "So, the whole affirmation goes",
    "I am STRONG!",
    "<sleep,0.2>",
    "I am BRAVE!",
    "<sleep,0.2>",
    "I can DO THIS!",
    "<sleep,0.2>",
    "OK, are you ready to show me how you do it?",
    "Here we go...",
    "I am STRONG!",
    "<sleep,0.2>",
    "I am BRAVE!",
    "<sleep,0.2>",
    "I can DO THIS!",
    "<sleep,0.2>",
    "Great job! Thanks for doing the affirmation with me.",
    "<sleep,0.2>",
    "That's all for today!",
]


def perform_script_2():
    for action in script2:
        if action == "<flex>":
            flex_motion()
            # time.sleep(0.1)
        elif action == "<hips>":
            hips_motion()
            # time.sleep(0.1)
        elif action == "<thumbs_up>":
            thumbs_up_motion()
            # time.sleep(0.1)
        elif action == "<zero>":
            zero_motion()
            # time.sleep(0.1)
        elif "<sleep" in action:
            splits = action.split(",")
            dur = float(splits[1][:-1])
            sleep_action(dur)
        else:
            tts.say(action)
        time.sleep(0.4)
    zero_motion()


# Start
if current_posture != "Stand":
    # Make NAO stand up
    posture_proxy.goToPosture("Stand", 2.0)

# # Call the function for flex motion
# flex.motion()

# Listening and speaking
with open("listen.txt", "w") as f:
    f.write("no")

with open("response.txt", "w") as f:
    f.write(" ")


# motion_proxy.setStiffnesses("RArm", 1.0)
# motion_proxy.setStiffnesses("LArm", 1.0)

# motion_proxy.setStiffnesses("Joints", 0.6)
# joints = left_arm_joints + right_arm_joints
# for joint in joints:
#     motion_proxy.setStiffnesses(joint, 0.6)

# motion_proxy.stiffnessInterpolation("Body", 1.0, 0.5)


perform_script_2()
# while True:
#     try:
#         with open("response.txt", "r") as f:
#             text = f.read().replace("\n", " ")

#         # have the NAO speak ChatGPT's response
#         if text != "":
#             if text != text_old:
#                 tracker_proxy.lookAt([2, 2, 0], 2, 0.5, False)
#                 # animated_speech.say(text)

#                 trigger_text = "[trigger;flex_motion]"

#                 # if "[trigger;flex_motion]" in text:
#                 #     flex_motion()

#                 old_index = text.find(trigger_text)
#                 new_text = ""
#                 if old_index != -1:
#                     index1 = old_index
#                     index2 = old_index + len(trigger_text)
#                     new_text = text[:index1] + " " + text[index2:]
#                     new_text1 = text[:index1]
#                     new_text2 = text[index2:]
#                     print(text)
#                     print(new_text)
#                     tts.say(new_text1)
#                     flex_motion()
#                     tts.say(new_text2)
#                 else:
#                     tts.say(text)

#                 if old_index != -1:
#                     zero_motion()

#                 print(new_text)
#                 text_old = text
#                 with open("listen.txt", "w") as f:
#                     f.write("yes")

#         time.sleep(1)
#     except Exception as e:
#         print("An error occurred: ", e)
#         time.sleep(1)
