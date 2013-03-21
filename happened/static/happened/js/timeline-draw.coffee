options =
    width:  "100%"
    height: "99%"
    style: "box"
    box: {align: "left"}
    min: min
    max: max

timeline = new links.Timeline document.getElementById 'timeline'
popup = $ '#popup'

# Add an after aspect to event select handler:
# When an event is selected, render the pop-up above it.
originalSelectItem = links.Timeline.prototype.selectItem

links.Timeline.prototype.selectItem = (index) ->
    originalSelectItem.call @, index
    if @items[index]?
        domItem = $ @items[index].dom
        popup.empty().insertBefore domItem
        popup.append domItem.find('p').clone()
        popup.append domItem.find('ul').clone()
        eventOffset = domItem.offset()
        popup.css
            'left': domItem.css 'left'
        popup.show()
        popup.css
            'top': domItem.css('top')[..-3] - popup.offset().height + 2 + 'px'
            'min-width': eventOffset.width - 6 + 'px'

# Add an after aspect to event unselect handler:
# When an event is unselected, hide the pop-up.
originalUnselectItem = links.Timeline.prototype.unselectItem

links.Timeline.prototype.unselectItem = ->
    popup.hide()
    originalUnselectItem.apply(this, arguments)

# When the timeline is scrolled or zoomed, unselect a selected event
# and hide the pop-up.  This fixes the problem where the pop-up
# wouldn't move together with the events.
links.events.addListener timeline, 'rangechanged',
    (object, event, properties) -> timeline.unselectItem()

# Draw the timeline.
timeline.draw data, options
