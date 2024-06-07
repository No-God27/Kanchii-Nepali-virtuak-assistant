if (!("webkitSpeechRecognition" in window)) {
  alert(
    "Web Speech API is not supported by this browser. Please upgrade to the latest version of Chrome."
  );
} else {
  const recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;

  const startBtn = document.getElementById("start-btn");
  const stopBtn = document.getElementById("stop-btn");
  const speechOutput = document.getElementById("speech-output");

  recognition.onstart = () => {
    startBtn.disabled = true;
    stopBtn.disabled = false;
    speechOutput.textContent = "Listening...";
  };

  recognition.onresult = (event) => {
    let interimTranscript = "";
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const transcript = event.results[i][0].transcript;
      if (event.results[i].isFinal) {
        speechOutput.textContent = transcript;
      } else {
        interimTranscript += transcript;
      }
    }
    speechOutput.textContent = interimTranscript;
  };

  recognition.onerror = (event) => {
    console.error(event.error);
    startBtn.disabled = false;
    stopBtn.disabled = true;
    speechOutput.textContent = "Error occurred in recognition: " + event.error;
  };

  recognition.onend = () => {
    startBtn.disabled = false;
    stopBtn.disabled = true;
    speechOutput.textContent = 'Press "Start Listening" to begin.';
  };

  startBtn.addEventListener("click", () => {
    recognition.start();
  });

  stopBtn.addEventListener("click", () => {
    recognition.stop();
  });
}
