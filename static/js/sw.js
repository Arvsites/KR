'use strict';
importScripts('/static/js/toolbox.js');
toolbox.router.get('/static/pwa-images/*', toolbox.cacheFirst);
toolbox.router.get('/', toolbox.networkFirst, { networkTimeoutSeconds: 5});