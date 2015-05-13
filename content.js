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
        console.log("send request to server......");
    	var xmlhttp;
    	xmlhttp = new XMLHttpRequest();

        xmlhttp.open( "GET", "http://130.126.255.36:1970/streams", false );
        xmlhttp.send(null);
        alert(xmlhttp.responseText);
        console.log(xmlhttp.responseText);
        console.log("Received......");
    	
    	
    	
    }
  });
