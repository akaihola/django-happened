(function() {
  var options, originalUnselectItem, popup, timeline;

  options = {
    width: "100%",
    height: "99%",
    style: "box",
    box: {
      align: "left"
    },
    cluster: false,
    min: min,
    max: max,
    editable: true,
    showButtonNew: true,
    showNavigation: true
  };

  timeline = new links.Timeline(document.getElementById('timeline'));

  popup = $('#popup');

  timeline.draw(data, options);

  $('div.timeline-event').click(function() {
    var event, eventOffset;
    event = $(this);
    popup.empty().insertBefore(event);
    popup.append($('p', this).clone());
    popup.append($('ul', this).clone());
    eventOffset = event.offset();
    popup.css({
      'left': event.css('left')
    });
    popup.show();
    return popup.css({
      'top': event.css('top').slice(0, -2) - popup.offset().height + 2 + 'px',
      'min-width': eventOffset.width - 6 + 'px'
    });
  });

  originalUnselectItem = links.Timeline.prototype.unselectItem;

  links.Timeline.prototype.unselectItem = function() {
    popup.hide();
    return originalUnselectItem.apply(this, arguments);
  };

}).call(this);
