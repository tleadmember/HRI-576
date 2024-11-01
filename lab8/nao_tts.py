import time
import naoqi
import math
from naoqi import ALProxy

# tts = ALProxy

ip = "10.60.237.164"  # ADJUST MANUALLY !!!

# text to speech proxy
tts = ALProxy("ALTextToSpeech", ip, 9559)

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

    fractionMaxSpeed = 0.2
    joints = left_arm_joints + right_arm_joints
    angles_radians_flex = left_arm_angles_radians_flex + right_arm_angles_radians_flex

    motion_proxy.setAngles(joints, angles_radians_flex, fractionMaxSpeed)

    time.sleep(1.0)
    # motion_proxy.setStiffnesses("Shoulder", 0.0)
    # motion_proxy.setStiffnesses("Elbow", 0.0)
    # motion_proxy.setStiffnesses("Wrist", 0.0)
    # motion_proxy.setStiffnesses("Hand", 0.0)


def zero_motion():
    # motion_proxy.setStiffnesses("Shoulder", 1.0)
    # motion_proxy.setStiffnesses("Elbow", 1.0)
    # motion_proxy.setStiffnesses("Wrist", 1.0)
    # motion_proxy.setStiffnesses("Hand", 1.0)

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
    # motion_proxy.setStiffnesses("Shoulder", 0.0)
    # motion_proxy.setStiffnesses("Elbow", 0.0)
    # motion_proxy.setStiffnesses("Wrist", 0.0)
    # motion_proxy.setStiffnesses("Hand", 0.0)


# Start
if current_posture != "Stand":
    # Make NAO stand up
    posture_proxy.goToPosture("StandInit", 1.0)

# # Call the function for flex motion
# flex.motion()

# Listening and speaking
with open("listen.txt", "w") as f:
    f.write("no")

with open("response.txt", "w") as f:
    f.write(" ")

while True:
    try:
        with open("response.txt", "r") as f:
            text = f.read().replace("\n", " ")

        # have the NAO speak ChatGPT's response
        if text != "":
            if text != text_old:
                tracker_proxy.lookAt([2, 2, 0], 2, 0.5, False)
                # animated_speech.say(text)

                trigger_text = "[trigger;flex_motion]"

                # if "[trigger;flex_motion]" in text:
                #     flex_motion()

                old_index = text.find(trigger_text)
                new_text = ""
                if old_index != -1:
                    index1 = old_index
                    index2 = old_index + len(trigger_text)
                    new_text = text[:index1] + " " + text[index2:]
                    new_text1 = text[:index1]
                    new_text2 = text[index2:]
                    print(text)
                    print(new_text)
                    tts.say(new_text1)
                    flex_motion()
                    tts.say(new_text2)
                else:
                    tts.say(text)

                if old_index != -1:
                    zero_motion()

                print(new_text)
                text_old = text
                with open("listen.txt", "w") as f:
                    f.write("yes")

        time.sleep(1)
    except Exception as e:
        print("An error occurred: ", e)
        time.sleep(1)
