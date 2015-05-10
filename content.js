/* Listen for messages */
// chrome.runtime.onMessage.addListener(function(msg, sender, sendResponse) {
//     /* If the received message has the expected format... */
//     if (msg.text && (msg.text == "report_back")) {
//         /* Call the specified callback, passing 
//            the web-pages DOM content as argument */
//         sendResponse(document.all[0].outerHTML);
//         alert(document.all[0].outerHTML)
//     }
// });

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    // console.log(sender.tab ?
    //             "from a content script:" + sender.tab.url :
    //             "from the extension");
    if (request.message == "message sent from background")
    {
    	var comments = document.getElementsByClassName("review-content");
    	alert(comments[0].textContent);
    	sendResponse({feedback: "response from content"});

    	var xmlhttp;
    	xmlhttp = new XMLHttpRequest();
    	xmlhttp.open("POST","http://localhost/index.html",true);
    	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    	xmlhttp.send("fname="+comments[0].textContent);
    }
  });
