from pupil_apriltags import Detector
import cv2

img =cv2.imread("test1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


at_detector = Detector(
   families="tag36h11",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

detect_result =  at_detector.detect(gray)
detect_result.center


