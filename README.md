# 🎙️ Faster-Whisper Voice Transcription

[![GitHub stars](https://img.shields.io/github/stars/AminePro7/faster-whisper?style=social)](https://github.com/AminePro7/faster-whisper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/AminePro7/faster-whisper?style=social)](https://github.com/AminePro7/faster-whisper/network/members)
[![GitHub issues](https://img.shields.io/github/issues/AminePro7/faster-whisper)](https://github.com/AminePro7/faster-whisper/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A real-time voice transcription tool using the faster-whisper library for efficient speech-to-text conversion.

## 🚀 Features

- 🎤 Real-time audio recording with spacebar control
- 📝 Fast and accurate speech-to-text transcription
- ⏱️ Timestamp-based file naming for easy organization
- 🧠 Uses the optimized "medium" Whisper model
- 💻 CPU-optimized for performance on standard hardware

## 📋 Requirements

- Python 3.7+
- PyAudio
- faster-whisper
- keyboard
- bitsandbytes

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/AminePro7/faster-whisper.git
cd faster-whisper
```

2. Install the required dependencies:
```bash
pip install faster-whisper pyaudio keyboard bitsandbytes
```

## 💻 Usage

Run the script:
```bash
python transcribe_mic.py
```

- Press and hold the **SPACE** key to start recording
- Release the **SPACE** key to stop recording and start transcription
- Press **Q** to quit the application

## 🧪 How It Works

1. The script initializes the Whisper model with optimized settings for CPU usage
2. When you press the space key, it starts recording audio from your microphone
3. Upon releasing the space key, it saves the audio file with a timestamp
4. The recorded audio is then transcribed using the Whisper model
5. The transcription is displayed in the console

## 📊 Performance

The script uses the "medium" Whisper model with int8 quantization for optimal performance on CPU. You can adjust the model size and parameters in the code to balance between accuracy and speed based on your hardware capabilities.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**AminePro7**

- GitHub: [@AminePro7](https://github.com/AminePro7)

---

⭐️ If you found this project helpful, please consider giving it a star on GitHub! ⭐️ 