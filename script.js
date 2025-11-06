const rotor = document.getElementById("rotor");
const coilTop = document.getElementById("coilTop");
const coilBottom = document.getElementById("coilBottom");
const statusText = document.getElementById("status");
const speedDisplay = document.getElementById("speedDisplay");

const onBtn = document.getElementById("onBtn");
const offBtn = document.getElementById("offBtn");
const reverseBtn = document.getElementById("reverseBtn");
const increaseBtn = document.getElementById("increaseBtn");
const decreaseBtn = document.getElementById("decreaseBtn");

let running = false;
let reverse = false;
let angle = 0;
let intervalId;
let speed = 3; // 1 = slow, 10 = fast

function rotateMotor() {
  if (!running) return;
  angle += reverse ? -speed : speed;
  rotor.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;
}

function startMotor() {
  if (!running) {
    running = true;
    statusText.textContent = "Status: Motor Running";
    coilTop.style.background = "red";
    coilBottom.style.background = "blue";
    intervalId = setInterval(rotateMotor, 30);
  }
}

function stopMotor() {
  running = false;
  clearInterval(intervalId);
  statusText.textContent = "Status: Motor OFF";
  coilTop.style.background = "orange";
  coilBottom.style.background = "orange";
}

function reverseCurrent() {
  if (!running) return;
  reverse = !reverse;
  if (reverse) {
    coilTop.style.background = "blue";
    coilBottom.style.background = "red";
    statusText.textContent = "Status: Motor Running (Reversed Current)";
  } else {
    coilTop.style.background = "red";
    coilBottom.style.background = "blue";
    statusText.textContent = "Status: Motor Running (Normal Current)";
  }
}

function increaseSpeed() {
  if (speed < 10) speed++;
  speedDisplay.textContent = `power: ${speed}`;
}

function decreaseSpeed() {
  if (speed > 1) speed--;
  speedDisplay.textContent = `power: ${speed}`;
}

onBtn.addEventListener("click", startMotor);
offBtn.addEventListener("click", stopMotor);
reverseBtn.addEventListener("click", reverseCurrent);
increaseBtn.addEventListener("click", increaseSpeed);
decreaseBtn.addEventListener("click", decreaseSpeed);
