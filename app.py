from flask import Flask, request, send_file, render_template, jsonify
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import os
import subprocess
import time

# Flask 앱 생성
app = Flask(__name__)

# MusicGen 모델 로드
model = MusicGen.get_pretrained("melody")

# 생성된 음악 파일 저장 디렉터리 설정
content_dir = os.path.join(os.getcwd())
os.makedirs(content_dir, exist_ok=True)  # 디렉터리가 없으면 생성

# 생성된 음악 파일 이름 리스트
generated_files = []

# 기본 라우트
@app.route("/")
def home():
    return render_template("index.html")  # HTML 파일 로드

# 음악 생성 라우트
@app.route("/generate", methods=["POST"])
def generate_music():
    # 요청에서 프롬프트와 길이 가져오기
    data = request.json
    prompt = data.get("prompt", "A calm acoustic guitar melody")
    duration = int(data.get("duration", 10))

    # MusicGen으로 음악 생성
    model.set_generation_params(duration=duration)
    generated_audio = model.generate([prompt])

    # 파일 저장 경로와 이름
    filename = prompt
    filepath = os.path.join(content_dir, filename)
    audio_write(filepath, generated_audio[0].cpu(), model.sample_rate)

    # 생성된 파일 이름 추가
    generated_files.append(filename)

    # 반환: 새로 생성된 파일 이름과 전체 파일 목록
    return jsonify({"file": filename, "files": generated_files})

# 생성된 음악 파일 제공 라우트
@app.route("/content/<filename>")
def serve_file(filename):
    filepath = os.path.join(content_dir, filename)
    return send_file(filepath, mimetype="audio/wav")

# ngrok 실행 함수
def start_ngrok():
    print("Starting ngrok...")
    ngrok_process = subprocess.Popen(['./ngrok', 'http', '5000'])
    time.sleep(5)  # ngrok 실행 대기
    try:
        response = subprocess.check_output(['curl', '-s', 'http://localhost:4040/api/tunnels'])
        for line in response.decode().split('\n'):
            if 'https' in line:
                print(f"ngrok URL: {line.strip().split(' ')[-1]}")  # ngrok URL 출력
                break
    except Exception as e:
        print(f"Failed to retrieve ngrok URL: {e}")

# Flask 실행
if __name__ == "__main__":
    start_ngrok()  # ngrok 실행
    app.run(port=5000)
