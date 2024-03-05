import cv2
import os
from source.model_detection import object_detection
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


def video_source(video: str):
    try:
        
        cap = cv2.VideoCapture(video)

        # Tentukan ukuran yang diinginkan
        new_width = 640
        new_height = 480

        # Loop untuk membaca dan meresize setiap frame
        while(cap.isOpened()):
            # Baca frame
            ret, frame = cap.read()

            # Periksa apakah frame berhasil dibaca
            if ret == True:
                # Resize frame
                resized_frame = cv2.resize(frame, (new_width, new_height))
                resized_frame = object_detection(resized_frame)

                # Tampilkan frame yang telah diresize
                cv2.imshow('Resized Frame', resized_frame)

                # Tunggu 25ms, tekan 'q' untuk keluar dari loop
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        # Bebaskan sumber video dan tutup semua jendela
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        raise Exception("Video Error")