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
    //alert("come into addListener");
    if(request.IsData == "true")
    {
        //alert(request.message);
        var marked_reviews_obj = JSON.parse(request.message);
        //alert(typeof marked_reviews_obj);
        //alert(marked_reviews_obj[0])
        comments_parent = document.querySelectorAll(".review-content p");
        for (var i = 0; i < comments_parent.length; i++){
            comments_parent[i].innerHTML = marked_reviews_obj[i]

        }
        var color_reviews = document.getElementsByClassName("mark_as_praise");
        for(var i = 0; i < color_reviews.length; i++){
            color_reviews[i].style.color = "magenta";

        }
        sendResponse("u got it, u got all colors now!");
    }
    else{
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
    
    

        for (var i = 0; i < comments.length; ++i){
            var each_comment_node = comments[i];
            comments_list[i.toString()] = each_comment_node.textContent;
        }
        var json = JSON.stringify(comments_list);
        //alert("pseudo json test");
        //alert("json test"+json);
        sendResponse(json);
    }
  });
