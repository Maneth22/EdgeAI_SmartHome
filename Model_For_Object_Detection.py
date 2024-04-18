from ultralytics import YOLO
import cv2


def yolo_pre():

    model = YOLO('yolov8n.pt')

    # load video
    cap = cv2.VideoCapture(0)

    ret = True
    # read frames

    while ret:
        ret, frame = cap.read()

        if ret:
            #results =  model.track(frame)
            results = model.track(frame, persist=True)
            
            person_count = 0
            
            # check if object with id 1 is detected
            for result in results:
                
                for c in result.boxes.cls:
                    print(model.names[int(c)])
                    
                    if model.names[int(c)] == 'person':
                        person_count += 1
                        
                    if person_count >= 1:
                        cap.release()
                        cv2.destroyAllWindows()
                    
            print(f"Number of persons detected: {person_count}")
                
            # plot results
            frame_ = results[0].plot()

            # visualize
            cv2.imshow('frame', frame_)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    
    return person_count


num_count = yolo_pre()
print(num_count)