const form = document.getElementById("music-form");
        const promptInput = document.getElementById("prompt");
        const loading = document.querySelector(".loading");
        const musicPlayer = document.getElementById("music-player");
        const musicList = document.getElementById("music-list");

        // 폼 제출 처리
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            loading.style.display = "block";
            musicPlayer.style.display = "none";

            const prompt = promptInput.value;
            const duration = document.getElementById("duration").value;

            const response = await fetch("/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ prompt, duration }),
            });

            if (response.ok) {
                const result = await response.json(); // 서버에서 파일 목록 가져오기
                updateMusicList(result.files); // 목록 업데이트
            } else {
                alert("Failed to generate music.");
            }

            loading.style.display = "none";
        });

        // 키워드 추가
        function addKeyword(keyword) {
            promptInput.value += ` ${keyword}`;
        }

        // 프롬프트 초기화
        function clearPrompt() {
            promptInput.value = "";
        }

        // 음악 목록 업데이트
        function updateMusicList(files) {
            musicList.innerHTML = ""; // 기존 목록 초기화

            files.forEach((file) => {
                const listItem = document.createElement("li"); // 목록 항목 생성
                const link = document.createElement("a"); // 음악 파일 링크 생성
                link.textContent = file;
                link.href = `/content/${file}.wav`;
                link.onclick = (e) => {
                    e.preventDefault();
                    musicPlayer.src = link.href; // 음악 파일 재생
                    musicPlayer.style.display = "block";
                    musicPlayer.play();
                };
                listItem.appendChild(link);
                musicList.appendChild(listItem);
            });
        }
