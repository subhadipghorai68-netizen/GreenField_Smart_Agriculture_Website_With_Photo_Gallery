const pumpButton = document.getElementById("pump-toggle");
const pumpStatus = document.getElementById("pump-status");
const pumpMessage = document.getElementById("pump-message");
let pumpIsOn = false;

pumpButton.addEventListener("click", async () => {
  const action = pumpIsOn ? "off" : "on";
  pumpButton.disabled = true;
  try {
    const response = await fetch("/api/irrigation", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({action})
    });
    const result = await response.json();
    if (!response.ok || !result.ok) throw new Error(result.message || "Request failed");
    pumpIsOn = action === "on";
    pumpButton.classList.toggle("on", pumpIsOn);
    pumpStatus.textContent = `Demo · ${result.status}`;
    pumpMessage.textContent = result.message;
  } catch (error) {
    pumpMessage.textContent = "Could not update the demo control. Please try again.";
  } finally {
    pumpButton.disabled = false;
  }
});

document.getElementById("advice-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const resultBox = document.getElementById("advice-result");
  resultBox.textContent = "Preparing suggestion…";
  try {
    const response = await fetch("/api/advice", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        crop: document.getElementById("crop").value,
        moisture: document.getElementById("moisture").value
      })
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.advice || "Please check your input.");
    resultBox.textContent = result.advice;
  } catch (error) {
    resultBox.textContent = error.message;
  }
});
