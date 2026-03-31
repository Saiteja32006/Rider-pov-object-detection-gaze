import cv2
import os
from pathlib import Path


def extract_frames_at_1fps(video_path, output_dir="extracted_frames"):
    """
    Extract frames from video at 1 frame per second

    Args:
        video_path: Path to the input video file
        output_dir: Directory to save extracted frames
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"Video Properties:")
    print(f"  FPS: {fps}")
    print(f"  Total Frames: {total_frames}")
    print(f"  Duration: {duration:.2f} seconds")
    print(f"  Expected output frames: {int(duration)}")
    print(f"\nExtracting frames at 1 FPS...")

    # Calculate frame interval (how many frames to skip)
    frame_interval = int(fps)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save frame every 'frame_interval' frames (i.e., every second)
        if frame_count % frame_interval == 0:
            # Create filename with timestamp
            timestamp = frame_count / fps
            filename = f"frame_{saved_count:04d}_t{timestamp:.2f}s.jpg"
            filepath = os.path.join(output_dir, filename)

            # Save frame
            cv2.imwrite(filepath, frame)
            saved_count += 1

            if saved_count % 10 == 0:
                print(f"  Saved {saved_count} frames...")

        frame_count += 1

    cap.release()
    print(f"\n✓ Extraction complete!")
    print(f"  Total frames saved: {saved_count}")
    print(f"  Output directory: {output_dir}")
    print(f"\nFrames are ready for upload to Roboflow!")


def main():
    # Example usage
    print("=" * 60)
    print("VIDEO FRAME EXTRACTOR (1 FPS)")
    print("=" * 60)

    # Set video path
    video_path = "scene_with_gaze.mp4"

    # Optional: custom output directory
    use_custom_dir = input(
        "Use custom output directory? (y/n, default: n): ").strip().lower()

    if use_custom_dir == 'y':
        output_dir = input("Enter output directory name: ").strip()
    else:
        output_dir = "extracted_frames"

    # Extract frames
    extract_frames_at_1fps(video_path, output_dir)

    print("\n" + "=" * 60)
    print("NEXT STEPS FOR ROBOFLOW ANNOTATION:")
    print("=" * 60)
    print("""
1. Go to https://roboflow.com/ and sign in
2. Create a new project (Object Detection)
3. Set up your classes:
   - pedestrian
   - two_wheeler
   - auto
   - car
   - bus_truck
   - intersection_conflict_zone
   - signs
   
4. Upload the extracted frames from: {}
5. Start annotating your objects!

Tip: You can upload all frames at once using batch upload.
    """.format(output_dir))


if __name__ == "__main__":
    main()
