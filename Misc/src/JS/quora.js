linkText = document.getElementsByClassName("link_text")
for (i = 0; i < linkText.length; i++){
    console.log(i +" " +linkText[i].innerText);
}

var hasClass = recursivelyWalk(element.childNodes, function hasClass(node) {
  return node.classList.contains("myClass");
});

function recursivelyWalk(nodes, cb) {
    for (var i = 0, len = nodes.length; i < len; i++) {
        var node = nodes[i];
        var ret = cb(node);
        if (ret) {
            return ret;
        }
        if (node.childNodes && node.childNodes.length) {
            var ret = recursivelyWalk(node.childNodes, cb);
            if (ret) {
                return ret;
            }
        }
    }
}

questionText = document.getElementsByClassName("QuestionText");
myString = "";
for (i = 0; i < questionText.length; i++){
    linkText = questionText[i].getElementsByClassName("link_text")
    if (linkText[0].children[0].innerText != ""){
        linkText[0].removeChild(linkText[0].childNodes[0])
    }
    myString += "* ["+linkText[0].innerText+"]" +"(" +questionText[i].getElementsByTagName("a")[0].href +") " +"  \n";
        
}

javascript:(function(){
    questionText = document.getElementsByClassName("QuestionText");
    myString = "";
    for (i = 0; i < questionText.length; i++){
        linkText = questionText[i].getElementsByClassName("link_text");
        if (linkText[0].children[0].innerText != ""){
            linkText[0].removeChild(linkText[0].childNodes[0]);
        }
        myString += "* ["+linkText[0].innerText+"]" +"(" +questionText[i].getElementsByTagName("a")[0].href +") " +"  \n";
            
    }
    console.log(myString)    
})();


followers = document.getElementsByClassName("ObjectCard-header");
myString = "\n";
for (i = 0; i < followers.length; i++){
    followersLink = followers[i].getElementsByTagName('a')
    myString += "* ["+followersLink[1].innerText+"]" +"(" +followersLink[0].href +") " +"  \n";        
}

javascript:(function(){
    followers = document.getElementsByClassName("ObjectCard-header");
    myString = "\n";
    for (i = 0; i < followers.length; i++){
        followersLink = followers[i].getElementsByTagName('a')
        myString += "* ["+followersLink[1].innerText+"]" +"(" +followersLink[0].href +"answers/Machine-Learning) " +"  \n";        
    }
    console.log(myString)    
})();
javascript:(function(){
for(followers=document.getElementsByClassName("ObjectCard-header"),myString="\n",i=0;i<followers.length;i++)followersLink=followers[i].getElementsByTagName("a"),myString+= i +" ["+followersLink[1].innerText+"]("+followersLink[0].href+"answers/Machine-Learning)   \n";console.log(myString);
})();



relatedQuestion = document.getElementsByClassName("related_questions");
unorderedList=relatedQuestion[0].getElementsByTagName('ul');
liNodes = unorderedList[0].childNodes;
myString = "\n";
for (i = 0; i < liNodes.length; i++){
    answerLink = liNodes[i].getElementsByTagName('a');
    myString += "* ["+answerLink[0].innerText+"]" +"(" +answerLink[0].href +"answers/Machine-Learning) " +"  \n";
}

