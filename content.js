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
var comment_section_tags = [".review-content p", "", "", ""];
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    // console.log(sender.tab ?
    //             "from a content script:" + sender.tab.url :
    //             "from the extension");
    if (request.message == "message sent from background")
    {
    	//var comments = document.getElementsByClassName("review-content");
        var comments = document.querySelectorAll(".review-content p");//Yelp specific
        var comments_list = {};
        for (var i = 0; i < comments.length; ++i){
            var each_comment_node = comments[i];
            comments_list[i.toString()] = each_comment_node.textContent;


        }
        var json = JSON.stringify(comments_list);
        alert("json test"+json);

        //comments[0].style.color = "magenta";

    	//alert(comments[0].textContent);
    	sendResponse(json);
     //    console.log("send request to server......");
    	// var xmlhttp;
    	// xmlhttp = new XMLHttpRequest();

     //    xmlhttp.open( "POST", "http://localhost:11200/streams", false );
     //    xmlhttp.send("hi!");
     //    alert(xmlhttp.responseText);
     //    console.log(xmlhttp.responseText);
     //    console.log("Received......");
    	
    	
    	
    }
  });
