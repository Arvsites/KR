function registerServiceWorker() {
// регистрирует скрипт sw в поддерживаемых браузерах
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('https://multimer.ru/static/js/sw.js', { scope: '/' }).then(() => {
      console.log('Service Worker registered successfully.');
    }).catch(error => {
      console.log('Service Worker registration failed:', error);
    });
  }
}