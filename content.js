/* Listen for messages */

//var comment_section_tags = [".review-content p"]
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
        var comments;
        var comments_list = {};
    alert("come into addListener");
    if (request.message.indexOf("yelp") > -1)
    {
        comments = document.querySelectorAll(".review-content p");//Yelp specific
    }
    else if(request.message.indexOf("walmart") > -1)
    {
        comments = document.querySelectorAll(".customer-review-text p");
    }
    else if(request.message.indexOf("tripadvisor") > -1)
    {
        comments = document.querySelectorAll(".partial_entry");
    }
    else
    {
        comments = document.querySelectorAll(".BVRRReviewText");
        console.log("come into else"); 
    }
       
    if(comments.length==0)
        alert("comments is null");
    else 
        alert(comments.length);
    for (var i = 0; i < comments.length; ++i){
        var each_comment_node = comments[i];
        comments_list[i.toString()] = each_comment_node.textContent;
    }
    var json = JSON.stringify(comments_list);
    alert("pseudo json test");
    alert("json test"+json);
    sendResponse(json);

  });
