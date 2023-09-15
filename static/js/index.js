if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker
      .register("/static/js/service-worker.js")
      .then(() => console.log("Service worker registered"))
      .catch(() => console.log("Service worker not registered"))
  })
}
