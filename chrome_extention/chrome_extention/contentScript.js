if(typeof init === 'undefined'){
const init=function(){
    var node = document.querySelector("#ppd")
    const injectElement = document.createElement('div');
    injectElement.className ='rustyZone-element';
    injectElement.innerHTML='Just for testing';
    node.parentNode.insertBefore(injectElement, node.nextSibling);
    // document.body.appendChild(injectElement);
    var url=window.location.href
    console.log(url);
}
init();
}