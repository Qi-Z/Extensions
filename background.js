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
            css: ["div.review-content", "div.media-story"]
          });

chrome.runtime.onInstalled.addListener(function() {
  // Replace all rules ...
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    // With a new rule ...
    chrome.declarativeContent.onPageChanged.addRules([
      {
        // That fires when a page's URL contains a 'g' ...
        conditions: [
          condition1, condition2
        ],
        // And shows the extension's page action.
        actions: [ new chrome.declarativeContent.ShowPageAction() ]
      }
    ]);
  });
});

chrome.pageAction.onClicked.addListener(function(){
  console.log("Before sending message")
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {message: "message sent from background"}, function(response) {
      console.log(response.feedback);
    });
  });

  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open("POST","http://localhost/index.html",true);
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.send("fname="+"sophiaaaaaaa");
  console.log("After sending message in background.js")
  //alert("After sending message")
});
