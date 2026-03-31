# Video Frame Extraction for Roboflow Annotation

This tool extracts frames from your video at 1 FPS (1 frame per second) for annotation in Roboflow.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install OpenCV directly:
```bash
pip install opencv-python
```

### 2. Run the Script

```bash
python video_frame_extractor.py
```

The script will prompt you for:
- Path to your video file
- (Optional) Custom output directory name

### 3. Output

Frames will be saved as:
- `frame_0000_t0.00s.jpg`
- `frame_0001_t1.00s.jpg`
- `frame_0002_t2.00s.jpg`
- etc.

Each filename includes:
- Frame number (sequential)
- Timestamp from original video

## Roboflow Classes

When setting up your Roboflow project, create these classes:

1. **pedestrian** - People walking or standing
2. **two_wheeler** - Motorcycles, scooters, bicycles
3. **auto** - Auto-rickshaws
4. **car** - Passenger cars
5. **bus_truck** - Buses and trucks (heavy vehicles)
6. **intersection_conflict_zone** - Areas where traffic paths cross
7. **signs** - Traffic signals, traffic signs, and billboards

## Roboflow Workflow

### Step 1: Create Project
1. Go to [Roboflow](https://roboflow.com/)
2. Create a new project
3. Choose "Object Detection"
4. Name your project (e.g., "Traffic Scene Detection")

### Step 2: Add Classes
Add all 7 classes listed above in your project settings

### Step 3: Upload Frames
1. Click "Upload" in your project
2. Select all extracted frames from the output directory
3. Batch upload (Roboflow handles multiple files)

### Step 4: Annotate
1. Use bounding boxes to label objects
2. Assign appropriate class to each box
3. Save annotations

### Step 5: Generate Dataset
1. Add preprocessing (optional): Auto-Orient, Resize
2. Add augmentation (optional): Flip, Rotation, Brightness
3. Generate dataset versions
4. Export in your preferred format (YOLO, COCO, etc.)

## Tips

- **1 FPS** is usually sufficient for traffic scenes (reduces redundancy)
- For fast-moving objects, consider extracting at 2-3 FPS
- Start with a subset of frames to test your annotation workflow
- Use Roboflow's keyboard shortcuts to speed up annotation
- Consider using Roboflow's Smart Polygon tool for complex shapes

## Troubleshooting

**Video won't open:**
- Check file path is correct
- Ensure video format is supported (mp4, avi, mov, etc.)

**Too many/few frames:**
- Adjust `frame_interval` in the script if needed
- For 2 FPS: change to `frame_interval = int(fps / 2)`

**Image quality issues:**
- Modify `cv2.imwrite()` quality parameter:
  ```python
  cv2.imwrite(filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
  ```

## Advanced Usage

To use the script programmatically:

```python
from video_frame_extractor import extract_frames_at_1fps

# Extract frames
extract_frames_at_1fps("path/to/video.mp4", "my_output_folder")
```

## License

Free to use for annotation and ML projects.
