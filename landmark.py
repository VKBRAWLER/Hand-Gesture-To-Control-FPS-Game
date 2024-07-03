import cv2
import mediapipe as mp

def main():
  # Initialize VideoCapture object
  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
  # Initialize mediapipe hands module
  mp_hands = mp.solutions.hands
  hands = mp_hands.Hands()

  while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert the BGR image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with mediapipe hands
    results = hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # Loop through all the landmarks and draw them on the frame
        for landmark in hand_landmarks.landmark:
          x = int(landmark.x * frame.shape[1])
          y = int(landmark.y * frame.shape[0])
          cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow('Hand Gesture Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Release the VideoCapture object and destroy all windows
  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()