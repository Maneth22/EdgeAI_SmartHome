from ultralytics import YOLO
import cv2
from gpiozero import MotionSensor
import time
from gpiozero import LED


def detection():
    # load yolov8 model
    start_time = time.time()
    model = YOLO('yolov8n.pt')

    # load video
    cap = cv2.VideoCapture(0)

    ret = True
    # read frames

    while ret:
        ret, frame = cap.read()

        if ret:
            # Perform inference
            # results = model(frame)
            # detect objects
            # results =  model.track(frame)
            results = model.track(frame, persist=True)

            person_count = 0

            # check if object with id 1 is detected
            for result in results:

                for c in result.boxes.cls:
                    print(model.names[int(c)])
                    current_time = time.time()
                    elapsedTime = current_time - start_time
                    if model.names[int(c)] == 'person':
                        person_count += 1
                        # print("Hello There is a person!!!")
                    # print(type(model.names[int(c)]))
                    if person_count >= 1:
                        cap.release()
                        cv2.destroyAllWindows()

                        return person_count
                    if elapsedTime >= 10:
                        cap.release()
                        cv2.destroyAllWindows()
                        print("no people found")
                        return 0

            # print(f"Number of persons detected: {person_count}")

            # plot results
            frame_ = results[0].plot()

            # visualize
            cv2.imshow('frame', frame_)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Print the list of detected objects
        # print(f"Detected objects: {detected_objects}")

        cap.release()
        cv2.destroyAllWindows()
    return 0

# pir = MotionSensor(17)
# def main():
#
#     while True:
#         num_people=0
#         #LED.off()
#         # while True:
#         pir.wait_for_motion()
#         num_people = detection()
#         while num_people>0:
#             led.on()
#             num_people=detection()
#         print(num_people)
#         # time.sleep(1)
#         #LED.on()
#         print("motion detected")
#         pir.wait_for_no_motion()
#         led.off()
#         # time.sleep(1)
#         print("motion not detected")
#         #LED.off()
