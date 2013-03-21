options =
    width:  "100%"
    height: "99%"
    style: "box"
    box: {align: "left"}
    cluster: false
    min: min
    max: max
    editable: true
    showButtonNew: true
    showNavigation: true

timeline = new links.Timeline document.getElementById 'timeline'
popup = $ '#popup'

timeline.draw data, options

onSelect = (object, event, properties) ->
    $event = $ this
    popup.empty().insertBefore $event
    popup.append $('p', this).clone()
    popup.append $('ul', this).clone()
    eventOffset = $event.offset()
    popup.css
        'left': $event.css 'left'
    popup.show()
    popup.css
        'top': $event.css('top')[..-3] - popup.offset().height + 2 + 'px'
        'min-width': eventOffset.width - 6 + 'px'

links.events.addListener timeline, 'select',
    (object, event, properties) -> onSelect.apply(this, object, event, properties)

# $('div.timeline-event').on 'click', onSelect

originalUnselectItem = links.Timeline.prototype.unselectItem

links.Timeline.prototype.unselectItem = ->
    popup.hide()
    originalUnselectItem.apply(this, arguments)

links.events.addListener timeline, 'rangechanged',
    (object, event, properties) -> popup.hide()
    