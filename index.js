//########## MODULES ##########
const Redirector = require("./redirector");

; (function () {
    "use strict"
    window.addEventListener("load", onStart, false);

    var redirector;

    function onStart(evt) {
        console.log("onStart");
        redirector = new Redirector();
        const urlParams = new URLSearchParams(window.location.search);
        const project = urlParams.get("project");
        const key = urlParams.get("key");
        redirector.redirect(project, key);
    }

})();