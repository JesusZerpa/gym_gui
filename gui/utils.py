def position(rect,rect_parent):
	if rect.bottomright:
		rect.x=rect_parent.width-rect.bottomright[1]
		rect.y=rect_parent.height-rect.bottomright[0]