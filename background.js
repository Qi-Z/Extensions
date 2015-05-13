// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// When the extension is installed or upgraded ...
var condition1 = new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'walmart' },
            css: ["div.customer-review-body"]
          });
var condition2 = new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'yelp' },
            css: ["div.review-content","div.media-story"]
          });
var condition3 = new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'tripadvisor' },
            css: ["div.entry"]
          });
var condition4 = new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'sephora' },
            css: ["span.BVRRReviewText"]
          });


chrome.runtime.onInstalled.addListener(function() {
  // Replace all rules ...
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    // With a new rule ...
    chrome.declarativeContent.onPageChanged.addRules([
      {
        // That fires when a page's URL contains a 'g' ...
        conditions: [
          condition1, condition2, condition3, condition4
        ],
        // And shows the extension's page action.
        actions: [ new chrome.declarativeContent.ShowPageAction() ]
      }
    ]);
  });
});
// var current_url;
// chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
//     var current_url = tabs[0].url;
// });
chrome.pageAction.onClicked.addListener(function(){
  console.log("Before sending message");

  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    console.log("Before getting url");
    var url = tabs[0].url;
    //alert(url);
    var response_text;
    chrome.tabs.sendMessage(tabs[0].id, {IsData: "false", message: url}, function(response) {
      //alert("come into sendMessage");

      var xmlhttp;
      xmlhttp = new XMLHttpRequest();
      xmlhttp.open("POST","http://localhost:11200/streams",false);
      xmlhttp.send(response);


      //alert(xmlhttp.responseText)
      response_text = xmlhttp.responseText;
       chrome.tabs.sendMessage(tabs[0].id, {IsData: "true", message: response_text}, function(response){
        //alert(response+"Last response");
        alert(response);
       });
    });
    //send classified reviews back to content.js

  });

  
});
