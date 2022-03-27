'use strict';
importScripts('/static/js/sw-toolbox.js.map'); toolbox.precache(["templates/main/main_page.html","/static/client/css/client.css"]); toolbox.router.get('/static/pwa-images/*', toolbox.cacheFirst); toolbox.router.get('/*', toolbox.networkFirst, { networkTimeoutSeconds: 5});
