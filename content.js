/* Listen for messages */
var comment_section_tags = [".review-content p"]
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
        var comments;
        var comments_list = {};
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
        comments = document.querySelectorAll(".entry p");
    }
    else
        comments = document.querySelectorAll(".BVRRReviewTextParagraph BVRRReviewTextFirstParagraph BVRRReviewTextLastParagraph p");

    for (var i = 0; i < comments.length; ++i){
        var each_comment_node = comments[i];
        comments_list[i.toString()] = each_comment_node.textContent;
    }
    var json = JSON.stringify(comments_list);
    alert("json test"+json);
    sendResponse(json);

  });
