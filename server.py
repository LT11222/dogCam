import cv2
import numpy
import socket
import time

def runServer():
    host = 'localhost'
    port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(1)
    s.bind((host, port))
    s.listen()

    cap = cv2.VideoCapture(0)

    while(True):
        (conn, address) = s.accept()
        ret, frame = cap.read()
        newframe = frame.flatten()
        newframe = newframe.tostring()
        conn.sendall(newframe)
        conn.sendall(b'0')
        conn.close()

        time.sleep(1)

    cap.release()

if __name__ == "__main__":
    runServer()
