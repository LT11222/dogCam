import cv2
import numpy
import socket
import time

def getImage():
    host = 'localhost'
    port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    frame = b''

    while len(frame) < 921600:
        part = s.recv(4096)
        frame += part

    s.shutdown(socket.SHUT_RDWR)
    s.close()

    frame = frame[:-1]

    newframe = numpy.fromstring(frame,dtype=numpy.uint8)
    newframe = newframe.reshape((480,640,3))

    return newframe

def runClient():

    while True:
        frame = getImage()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        runClient()
