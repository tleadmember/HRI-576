import time
import naoqi
import math
from naoqi import ALProxy

# tts = ALProxy

ip = "10.60.59.193"  # ADJUST MANUALLY !!!

# text to speech proxy
tts = ALProxy("ALTextToSpeech", ip, 9559)
tts.setParameter("speed", 92)

# animated speech proxy
animated_speech = ALProxy("ALAnimatedSpeech", ip, 9559)

# posture proxy
posture_proxy = ALProxy("ALRobotPosture", ip, 9559)

current_posture = posture_proxy.getPosture()

# gaze-related proxies
awareness_proxy = ALProxy("ALBasicAwareness", ip, 9559)
awareness_proxy.setEngagementMode("FullyEngaged")
awareness_proxy.setEnabled(True)
# awareness_proxy.setStimulusDetectionEnabled("Touch", True)

# gaze-related proxies
tracker_proxy = ALProxy("ALTracker", ip, 9559)

text_old = ""


# motion proxy
motion_proxy = ALProxy("ALMotion", ip, 9559)


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
    left_arm_angles_radians_thumbs_up = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_thumbs_up
    ]

    fractionMaxSpeed = 0.3
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

    fractionMaxSpeed = 0.3
    joints = left_arm_joints + right_arm_joints
    angles_radians_hips = left_arm_angles_radians_hips + right_arm_angles_radians_hips

    motion_proxy.setAngles(joints, angles_radians_hips, fractionMaxSpeed)

    time.sleep(1.0)


# Flex motion
def flex_motion():
    # motion_proxy.setStiffnesses("Shoulder", 1.0)
    # motion_proxy.setStiffnesses("Elbow", 1.0)
    # motion_proxy.setStiffnesses("Wrist", 1.0)
    # motion_proxy.setStiffnesses("Hand", 1.0)

    right_arm_angles_degrees_flex = [-4.6, -68.6, 86.7, 88.5, 75.4, 0.0]
    right_arm_angles_radians_flex = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_flex
    ]
    left_arm_angles_degrees_flex = [-8.8, 70.0, -75.1, -87.6, -72.0, 0.02]
    left_arm_angles_radians_flex = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_flex
    ]

    fractionMaxSpeed = 0.25
    joints = left_arm_joints + right_arm_joints
    angles_radians_flex = left_arm_angles_radians_flex + right_arm_angles_radians_flex

    motion_proxy.setAngles(joints, angles_radians_flex, fractionMaxSpeed)

    time.sleep(1.0)
    # motion_proxy.setStiffnesses("Shoulder", 0.0)
    # motion_proxy.setStiffnesses("Elbow", 0.0)
    # motion_proxy.setStiffnesses("Wrist", 0.0)
    # motion_proxy.setStiffnesses("Hand", 0.0)


def zero_motion():

    right_arm_angles_degrees_zero = [85.1, -12.7, 67.4, 22.6, 7.1, 0.5]
    right_arm_angles_radians_zero = [
        deg_to_rad(angle) for angle in right_arm_angles_degrees_zero
    ]
    left_arm_angles_degrees_zero = [82.9, 11.9, -70.1, -23.2, 4.2, 0.5]
    left_arm_angles_radians_zero = [
        deg_to_rad(angle) for angle in left_arm_angles_degrees_zero
    ]

    fractionMaxSpeed = 0.3
    joints = left_arm_joints + right_arm_joints
    angles_radians_zero = left_arm_angles_radians_zero + right_arm_angles_radians_zero

    motion_proxy.setAngles(joints, angles_radians_zero, fractionMaxSpeed)

    # motion_proxy.setStiffnesses("RArm", 0.0)
    # motion_proxy.setStiffnesses("LArm", 0.0)
    time.sleep(1.0)


script2 = [
    "Hello Friend! My name is Mentor, and I'm your coach today.",
    "For our first exercise, we are going to do an affirmation together.",
    "Don't worry, I'll explain how it works before we begin.",
    "Here's what we do",
    "First, we flex our arms over our head like this",
    "<flex>",
    "and we say, I am STRONG!",
    "Then, we put our hands on our hips like this",
    "<hips>",
    "and say, I am BRAVE!",
    "Then, we give two thumbs up like this",
    "<thumbs_up>",
    "and say, I can DO THIS!",
    "<zero>",
    "So, the entire affirmation goes",
    "<flex>",
    "I am STRONG!",
    "<hips>",
    "I am brave!",
    "<thumbs_up>",
    "I CAN DO THIS!",
    "<zero>",
    "OK, are you ready to do it with me?",
    "Here we go...",
    "<flex>",
    "I am STRONG!",
    "<hips>",
    "I am BRAVE!",
    "<thumbs_up>",
    "I can DO THIS!",
    "<zero>",
    "Great job! Thanks for doing the affirmation with me. That's all for today's exercises.",
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
        else:
            tts.say(action)
        time.sleep(0.5)
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

motion_proxy.stiffnessInterpolation("Body", 1.0, 0.5)

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
