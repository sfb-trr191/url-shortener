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