(function() {
    options = {"width":  "100%",
               "height": "99%",
               "style": "box"};

    var timeline = new links.Timeline(
        document.getElementById('timeline'));

    timeline.draw(data, options);
})();
