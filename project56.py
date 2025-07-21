from playsound import playsound

# Dictionary linking moods to audio file paths
mood_audio = {
    "1": "happy_song.mp3",
    "2": "sad_song.mp3",
    "3": "relaxed_ambient.mp3",
    "4": "angry_rock.mp3",
    "5": "confident_beats.mp3",
    "6": "focused_lofi.mp3"
}

# Display mood options
print("🎧 Choose your mood:")
print("1. 😊 Happy")
print("2. 😢 Sad")
print("3. 😌 Relaxed")
print("4. 😡 Angry")
print("5. 😎 Confident")
print("6. 🤔 Focused")

# Get user input
choice = input("Enter the number for your mood (1–6): ")

# Play audio based on mood
if choice in mood_audio:
    print(f"Playing audio for mood {choice}...")
    playsound(mood_audio[choice])
else:
    print("Invalid selection. Please choose a number from 1 to 6.")
