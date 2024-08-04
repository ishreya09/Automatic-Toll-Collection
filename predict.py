import cv2
import pytesseract
from ultralytics import YOLO
import re

# Configure the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update this path if needed

# Load YOLO model
model = YOLO('best.pt')

# Load video
video_path = "demo.mp4"
cap = cv2.VideoCapture(video_path)

# Define codec and create VideoWriter object to save output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_path = 'demo-output.avi'
out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

license_plates = []

def preprocess_plate_number(plate_text):
    # Remove special characters and spaces
    plate_text = re.sub(r'[^A-Za-z0-9]', '', plate_text)
    # Capitalize all alphabets
    plate_text = plate_text.upper()
    # Ensure uniqueness
    plate_text = ''.join(sorted(set(plate_text), key=plate_text.index))
    return plate_text

def clean_license_plates(license_plates):
    cleaned_plates = []
    for plate in license_plates:
        cleaned_plate = preprocess_plate_number(plate)
        if len(cleaned_plate) > 2:  # Remove length less than or equal to 2
            cleaned_plates.append(cleaned_plate)
    return list(set(cleaned_plates))  # Ensure uniqueness

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the current frame
    results = model(frame)

    # Process each result
    for result in results:
        # Access the boxes
        boxes = result.boxes.xyxy.cpu().numpy()  # Convert to numpy array
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate_image = frame[y1:y2, x1:x2]
            # Perform OCR on the detected plate
            plate_text = pytesseract.image_to_string(plate_image, config='--psm 8').strip()
            if plate_text:
                plate_text = preprocess_plate_number(plate_text)
                if plate_text not in license_plates:
                    license_plates.append(plate_text)
                # Draw bounding box and text
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, plate_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Write the frame to the output video
    out.write(frame)

# Release video capture and writer objects
cap.release()
out.release()

# Clean the final list of license plates
cleaned_plates = clean_license_plates(license_plates)
print(f'Cleaned license plates: {cleaned_plates}')
print(f'Processed video saved to: {output_path}')
