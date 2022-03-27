'use strict';
importScripts('/static/js/sw-toolbox.js.map');
toolbox.router.get('/static/pwa-images/*', toolbox.cacheFirst);
toolbox.router.get('/*', toolbox.networkFirst, { networkTimeoutSeconds: 5});
