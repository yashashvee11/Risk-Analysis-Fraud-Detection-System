var circularProgress = document.querySelectorAll(".circular-progress");

Array.from(circularProgress).forEach((progressBar) => {
  const progressValue = progressBar.querySelector(".percentage");
  const innerCircle = progressBar.querySelector(".inner-circle");
  let startValue = 0,
    endValue = Number(progressBar.getAttribute("data-percentage")),
    speed = 25,
    progressColor = progressBar.getAttribute("data-progress-color");

  const progress = setInterval(() => {
    startValue++;
    progressValue.textContent = `${startValue}%`;
    progressValue.style.color = `${progressColor}`;

    innerCircle.style.backgroundColor = `${progressBar.getAttribute(
      "data-inner-circle-color"
    )}`;

    progressBar.style.background = `conic-gradient(${progressColor} ${
      startValue * 3.6
    }deg,${progressBar.getAttribute("data-bg-color")} 0deg)`;
    if (startValue === endValue) {
      clearInterval(progress);
    }
  }, speed);
});

// OnSeacrh loader event
var queryInput = document.getElementsByClassName("query")[0];
var loader = document.getElementById("loader");
queryInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        loader.style.display = 'block';
    }
});

// OnPurge loader event
var purgeBtn = document.getElementsByClassName("purge-btn")[0];
var purgeLoader = document.getElementById("purge-loader");
purgeBtn.addEventListener("click", function(event) {
    purgeLoader.style.display = 'block';
});
