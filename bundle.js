(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
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
},{"./redirector":2}],2:[function(require,module,exports){
class Redirector {

    constructor() {

    }

    redirect(project, key) {
        var path = "redirections/"+project+"/"+key+".txt"
        console.log("get redirection url: ", path);
        var redirection_url = this.loadFile(path);
        console.log("redirection_url: ", redirection_url);
        if(redirection_url)
            window.location.href = redirection_url;
    }

    loadFile(filePath) {
        var result = null;
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", filePath, false);
        xmlhttp.send();
        if (xmlhttp.status==200) {
          result = xmlhttp.responseText;
        }
        return result;
      }
}

module.exports = Redirector;
},{}]},{},[1]);
