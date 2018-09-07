try:
    import logging
    import colorlog
    import logging.config
    import sys
    if __debug__:
        logging.config.fileConfig('logging.conf')
        logger = colorlog.getLogger('loggingUser')
    else:
        logging.config.fileConfig('service.conf')
        logger = colorlog.getLogger('loggingUser')
    import time
    import face_recognition
    import cv2
    from datetime import datetime, timedelta
except Exception as e:
    logging.warning("Error importing libraries {}".format(e))
    sys.exit()
    
def enconde(face):
    face_now = face_recognition.load_image_file(face)
    encoding = face_recognition.face_encodings(face_now)[0]
    return enconding 


def detect_face():
    faces = []
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for face in face_encodings:
        matches = face_recognition.compare_faces(known, face, 0.5)
        if True in matches:
            logging.debug('It\'s a match!!')
            logging.warning('the len of known is {}'.format(len(known)))
        else:
            logging.debug('new face, going to append')
            known.append(face)


if __name__ == '__main__':
    video_capture = cv2.VideoCapture(0)
    face_locations = []
    face_encodings = []
    known = []
    while True:
        faces = detect_face()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
