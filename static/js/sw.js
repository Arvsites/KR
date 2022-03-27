'use strict';
importScripts('toolbox.js');
toolbox.router.get('/static/pwa-images/*', toolbox.cacheFirst);
toolbox.router.get('/', toolbox.networkFirst, { networkTimeoutSeconds: 5});