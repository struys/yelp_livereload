LiveReloadPluginSCSS = function(window, host) {
    this.window = window;
    this.host = host;
};

LiveReloadPluginSCSS.prototype.reload = function(path, options) {
    var isScss = path.match(/\.scss$/);
    if (isScss) {
        var links = document.getElementsByTagName('link');
        for (var i = 0; i < links.length; i++) {
            var link = links[i];
            if(link.rel === 'stylesheet') {
                link.href = this.host.generateCacheBustUrl(link.href);
            }
        }
    }

    return isScss;
};
