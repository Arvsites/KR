'use strict';
importScripts('https://multimer.ru/static/js/sw-toolbox.js.map');
toolbox.router.get('https://multimer.ru/static/pwa-images/*', toolbox.cacheFirst);
toolbox.router.get('https://multimer.ru/*', toolbox.networkFirst, { networkTimeoutSeconds: 5});
