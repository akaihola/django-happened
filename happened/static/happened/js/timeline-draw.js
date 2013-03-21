(function() {
  var onSelect, options, originalUnselectItem, popup, timeline;

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

  onSelect = function(object, event, properties) {
    var $event, eventOffset;
    $event = $(this);
    popup.empty().insertBefore($event);
    popup.append($('p', this).clone());
    popup.append($('ul', this).clone());
    eventOffset = $event.offset();
    popup.css({
      'left': $event.css('left')
    });
    popup.show();
    return popup.css({
      'top': $event.css('top').slice(0, -2) - popup.offset().height + 2 + 'px',
      'min-width': eventOffset.width - 6 + 'px'
    });
  };

  links.events.addListener(timeline, 'select', function(object, event, properties) {
    return onSelect.apply(this, object, event, properties);
  });

  originalUnselectItem = links.Timeline.prototype.unselectItem;

  links.Timeline.prototype.unselectItem = function() {
    popup.hide();
    return originalUnselectItem.apply(this, arguments);
  };

  links.events.addListener(timeline, 'rangechanged', function(object, event, properties) {
    return popup.hide();
  });

}).call(this);
