import cv2
import numpy as np

# Create a blank white image (500x500 pixels)
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw some mock "bubbles" (circles) for the OMR sheet
# row 1
cv2.circle(img, (100, 100), 20, (0, 0, 0), 2)  
cv2.circle(img, (200, 100), 20, (0, 0, 0), 2)  # Filled bubble
cv2.circle(img, (300, 100), 20, (0, 0, 0), 2)
cv2.circle(img, (400, 100), 20, (0, 0, 0), 2)

# Fill one bubble to simulate a student's answer
cv2.circle(img, (200, 100), 18, (50, 50, 50), -1)

# row 2
cv2.circle(img, (100, 200), 20, (0, 0, 0), 2)
cv2.circle(img, (200, 200), 20, (0, 0, 0), 2)
cv2.circle(img, (300, 200), 20, (0, 0, 0), 2) # Filled bubble
cv2.circle(img, (400, 200), 20, (0, 0, 0), 2)

# Fill another bubble
cv2.circle(img, (300, 200), 18, (50, 50, 50), -1)

# Save it as test_omr.png
cv2.imwrite("test_omr.png", img)
print("test_omr.png generated successfully!")