const staticGraphQLPWADemo = "flask-graphql-pwa-demo-v1"
const assets = [
  "/",
  "/static/images/logo.svg",
  "/static/js/index.js",
  "static/js/service-worker.js",
  "static/manifest.json",
]

self.addEventListener("install", (installEvent) => {
  installEvent.waitUntil(
    caches.open(staticGraphQLPWADemo).then((cache) => {
      cache.addAll(assets)
    })
  )
})

self.addEventListener("fetch", (fetchEvent) => {
  fetchEvent.respondWith(
    caches.match(fetchEvent.request).then((res) => {
      return res || fetch(fetchEvent.request)
    })
  )
})
